from nonebot import on_message, on_command
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot_plugin_guild_patch import GuildMessageEvent

from .data_source import send_msg_to_mc, send_command_to_mc
from ...utils import msg_rule, permission_check
from typing import Union

mc_qq = on_message(priority=5, rule=msg_rule, block=False)
mc_qq_command = on_command(
    "mcc",
    priority=3,
    rule=msg_rule
)
mc_qq_command.handle()(permission_check)


# 收到 群/频 道消息时
@mc_qq.handle()
async def handle_first_receive(bot: Bot, event: Union[GroupMessageEvent, GuildMessageEvent]):
    await send_msg_to_mc(bot=bot, event=event)


# 收到 群/频道 命令时
@mc_qq_command.handle()
async def handle_first_receive(bot: Bot, event: Union[GroupMessageEvent, GuildMessageEvent]):
    await send_command_to_mc(bot=bot, event=event)
