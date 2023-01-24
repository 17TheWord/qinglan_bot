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

add_sub = on_command("开启互通", rule=to_me(), priority=3)
add_sub.__doc__ = """开启互通 Server（群聊丨管理员）"""

add_sub.handle()(permission_check)

add_sub.handle()(handle_server_name)

add_sub.got("server_name", prompt="请输入要开启互通的服务器名")(server_name_check)


@add_sub.handle()
async def _(event: Union[GroupMessageEvent, GuildMessageEvent], server_name: str = ArgPlainText("server_name")):
    """根据服务器名 开启互通"""

    if isinstance(event, GuildMessageEvent):
        await db.add_guild(
            guild_id=event.guild_id, channel_id=event.channel_id, send_group_name=False
        )

    result = await db.add_sub(
        type=event.message_type,
        type_id=await get_type_id(event),
        server_name=server_name,
        display_server_name=False
    )

    if result:
        await add_sub.finish(message=f"已开启与服务器 {server_name} 的互通")
    await add_sub.finish(message=f"服务器 {server_name} 的互通已经开启过了")
