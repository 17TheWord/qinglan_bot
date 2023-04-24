from pathlib import Path
from typing import Optional, List

from nonebot import get_driver
from pydantic import BaseModel
from tortoise import Tortoise, connections
from .models import Sub, Server, Group, Guild


def get_path(*other):
    """获取数据文件绝对路径"""
    from .. import plugin_config

    dir_path = Path(plugin_config.mc_qq_dir if plugin_config.mc_qq_dir else "./data/")
    if not Path(dir_path).exists():
        dir_path.mkdir()
    dir_path = dir_path.resolve()
    return str(dir_path.joinpath(*other))


class GroupConfig(BaseModel):
    """群配置"""
    type: str
    type_id: int
    display_server_name: Optional[bool] = False


class MinecraftServer(BaseModel):
    """服务器配置"""
    # 服务器名称
    server_name: str
    # 服务器群列表
    all_group_list: Optional[List[GroupConfig]] = []
    # 是否用 Rcon 发送消息
    rcon_msg: Optional[bool] = False
    # 是否用 Rcon 发送命令
    rcon_cmd: Optional[bool] = False


server_list: List[MinecraftServer] = []
rule_group_list: List[int] = []
rule_guild_list: List[str] = []


class DB:
    """数据库交互类，与增删改查无关的部分不应该在这里面实现"""

    @classmethod
    async def init(cls):
        """初始化数据库"""
        from . import models
        await Tortoise.init(
            config={
                "connections": {
                    # "qinglan_bot": {
                    #     "engine": "tortoise.backends.sqlite",
                    #     "credentials": {"file_path": get_path("mcqq.sqlite3")},
                    # },
                    "qinglan_bot": f"sqlite://{get_path('mcqq.sqlite3')}"
                },
                "apps": {
                    "qinglan_app": {
                        "models": [models],  # 数据库
                        "default_connection": "qinglan_bot"
                    }
                }
            }
        )
        await Tortoise.generate_schemas()
        await cls.update_server_list()

    @classmethod
    async def get_server(cls, **kwargs):
        """获取 Server 信息"""
        return await Server.get(**kwargs).first()

    # 服务器 相关操作
    @classmethod
    async def add_server(cls, **kwargs):
        """添加 Server 信息"""
        return await Server.add(**kwargs)

    @classmethod
    async def delete_server(cls, server_name) -> bool:
        """删除 Server 信息"""
        if await cls.get_server(server_name=server_name):
            # 还存在该 UP 主订阅，不能删除
            return False
        await Server.delete(server_name=server_name)
        return True

    @classmethod
    async def update_server(cls, conf, switch, **kwargs):
        """更新服务器设置"""
        if await Server.update(kwargs, **{conf: switch}):
            await cls.update_server_list()
            return True
        return False

    # 群 相关操作
    @classmethod
    async def get_group(cls, **kwargs):
        """获取群设置"""
        return await Group.get(**kwargs).first()

    @classmethod
    async def add_group(cls, **kwargs):
        """创建群设置"""
        return await Group.add(**kwargs)

    @classmethod
    async def delete_group(cls, type_id) -> bool:
        """删除群设置"""
        if await cls.get_sub(type="group", type_id=type_id):
            # 当前群还有订阅，不能删除
            return False
        await Group.delete(group_id=type_id)
        return True

    @classmethod
    async def update_group(cls, group_id, switch):
        """设置指定群组权限"""
        if not await Group.update({"group_id": group_id}, send_group_name=switch):
            await cls.add_group(group_id=group_id, send_group_name=switch)

    # 频道 相关操作
    @classmethod
    async def get_guild(cls, **kwargs):
        """获取频道设置"""
        return await Guild.get(**kwargs).first()

    @classmethod
    async def add_guild(cls, **kwargs):
        """创建频道设置"""
        return await Guild.add(**kwargs)

    @classmethod
    async def delete_guild(cls, type_id) -> bool:
        """删除子频道设置"""
        if await cls.get_sub(type="guild", type_id=type_id):
            # 当前频道还有订阅，不能删除
            return False
        await Guild.delete(id=type_id)
        return True

    @classmethod
    async def update_guild(cls, guild_id, channel_id, switch):
        """设置指定群组权限"""
        if not await Guild.update({"guild_id": guild_id, "channel_id": channel_id},
                                  send_group_name=switch):
            await cls.add_guild(guild_id=guild_id, channel_id=channel_id, send_group_name=switch)

    @classmethod
    async def get_guild_type_id(cls, guild_id, channel_id) -> Optional[int]:
        """获取频道订阅 ID"""
        guild = await Guild.get(guild_id=guild_id, channel_id=channel_id).first()
        return guild.id if guild else None

    # 列表 相关操作
    @classmethod
    async def get_sub(cls, **kwargs):
        """获取指定位置的 互通列表"""
        return await Sub.get(**kwargs).first()

    @classmethod
    async def add_sub(cls, *, server_name, **kwargs) -> bool:
        """添加互通服务器"""
        if not await Sub.add(server_name=server_name, **kwargs):
            return False
        if kwargs["type"] == "group":
            await cls.add_group(group_id=kwargs["type_id"], send_group_name=False)
        if not await Server.get(server_name=server_name):
            await cls.add_server(
                server_name=server_name,
                rcon_ip="127.0.0.1",
                rcon_port=25575,
                rcon_password="change_password",
                rcon_msg=False,
                rcon_cmd=False
            )
        await cls.update_server_list()
        return True

    @classmethod
    async def set_sub(cls, conf, switch, **kwargs):
        """开关互通设置"""
        return await Sub.update(kwargs, **{conf: switch})

    @classmethod
    async def delete_sub(cls, server_name, type, type_id) -> bool:
        """删除指定互通记录"""
        if await Sub.delete(server_name=server_name, type=type, type_id=type_id):
            await cls.delete_server(server_name=server_name)
            await cls.update_server_list()
            return True
        # 订阅不存在
        return False

    @classmethod
    async def get_subs(cls, **kwargs):
        return await Sub.get(**kwargs)

    @classmethod
    async def get_sub_list(cls, type, type_id) -> List[Sub]:
        """获取指定位置的互通列表"""
        return await cls.get_subs(type=type, type_id=type_id)

    @classmethod
    async def delete_sub_list(cls, type, type_id):
        """删除指定位置的互通列表"""
        async for sub in await Sub.get(type=type, type_id=type_id):
            await cls.delete_sub(server_name=sub.server_name, type=sub.type, type_id=sub.type_id)
        await cls.update_server_list()

    @classmethod
    async def update_server_list(cls):
        """更新需要推送的 服务器 主列表"""
        subs = Sub.all()
        servers = Server.all()
        server_list.clear()
        async for server in servers:
            server_list.append(MinecraftServer(
                server_name=server.server_name,
                all_group_list=[],  # 服务器的所有群聊列表
                rcon_msg=server.rcon_msg,
                rcon_cmd=server.rcon_cmd
            ))

        for per_server in server_list:
            async for sub in subs:
                if per_server.server_name == sub.server_name:
                    # 向全群聊列表里装入每个互通记录
                    per_server.all_group_list.append(GroupConfig(
                        type=sub.type,
                        type_id=sub.type_id,
                        display_server_name=sub.display_server_name
                    ))
        groups = Group.all()
        async for group in groups:
            rule_group_list.append(group.group_id)
        guilds = Guild.all()
        async for guild in guilds:
            rule_guild_list.append(f"{guild.guild_id}:{guild.channel_id}")


get_driver().on_startup(DB.init)
get_driver().on_shutdown(connections.close_all)
