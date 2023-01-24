from typing import Union

from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.internal.params import ArgPlainText
from nonebot_plugin_guild_patch import GuildMessageEvent

from ...database import DB as db

from ...utils import (
    handle_server_name,
    server_name_check,
    get_type_id,
    permission_check,
    to_me
)

delete_sub = on_command("关闭互通", rule=to_me(), priority=3)
delete_sub.__doc__ = """关闭互通 Server（群聊丨管理员）"""

delete_sub.handle()(permission_check)

delete_sub.handle()(handle_server_name)

delete_sub.got("server_name", prompt="请输入要关闭互通的服务器名")(server_name_check)


@delete_sub.handle()
async def _(event: Union[GroupMessageEvent, GuildMessageEvent], server_name: str = ArgPlainText("server_name")):
    """根据服务器名 关闭互通"""
    servername = getattr(await db.get_server(server_name=server_name), "server_name", None)

    if servername:
        result = await db.delete_sub(
            type=event.message_type,
            type_id=await get_type_id(event),
            server_name=server_name
        )
    else:
        result = False

    if result:
        await delete_sub.finish(message=f"已关闭与服务器 {server_name} 的互通")
    await delete_sub.finish(message=f"服务器 {server_name} 的互通未开启")
