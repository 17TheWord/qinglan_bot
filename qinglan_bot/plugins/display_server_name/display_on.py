from typing import Union

from nonebot import on_command
from nonebot.adapters.onebot.v11.event import GroupMessageEvent
from nonebot.params import ArgPlainText
from nonebot_plugin_guild_patch import GuildMessageEvent

from ...database import DB as db
from ...utils import get_type_id, permission_check, handle_server_name, server_name_check, to_me

display_on = on_command("开启服务器名", rule=to_me(), priority=3)
display_on.__doc__ = """开启服务器名 Server（管理员）"""

display_on.handle()(permission_check)

display_on.handle()(handle_server_name)

display_on.got("server_name", prompt="请输入要开启显示服务器名的服务器")(server_name_check)


@display_on.handle()
async def _(event: Union[GroupMessageEvent, GuildMessageEvent], server_name: str = ArgPlainText("server_name")):
    """根据 服务器名 开启 显示服务器名"""
    if await db.set_sub(
            "display_server_name",
            True,
            server_name=server_name,
            type=event.message_type,
            type_id=await get_type_id(event)
    ):
        server = await db.get_server(server_name=server_name)
        assert server is not None
        await display_on.finish(f"已开启 [{server.server_name}] 的显示服务器名")
    await display_on.finish(f"服务器（{server_name}）未互通，请先互通后再操作")
