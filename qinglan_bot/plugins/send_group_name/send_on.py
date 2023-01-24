from typing import Union

from nonebot import on_command
from nonebot.adapters.onebot.v11.event import GroupMessageEvent
from nonebot_plugin_guild_patch import GuildMessageEvent

from ...database import DB as db
from ...utils import permission_check, to_me

send_on = on_command("开启发送群名", rule=to_me(), priority=3)
send_on.__doc__ = """开启发送群名（群聊丨管理员）"""

send_on.handle()(permission_check)


@send_on.handle()
async def _(event: Union[GroupMessageEvent, GuildMessageEvent]):
    """开启 发送群名"""
    if isinstance(event, GroupMessageEvent):
        if await db.update_group(group_id=event.group_id, switch=True):
            group = await db.get_group(group_id=event.group_id)
            assert group is not None
    else:
        if await db.update_guild(guild_id=event.guild_id, channel_id=event.channel_id, switch=True):
            guild = await db.get_guild(guild_id=event.guild_id, channel_id=event.channel_id)
            assert guild is not None
    await send_on.finish(f"已开启本群聊的发送群名")
