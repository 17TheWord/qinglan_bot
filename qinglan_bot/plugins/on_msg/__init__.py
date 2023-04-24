from nonebot import on_message, on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot_plugin_guild_patch import GuildMessageEvent
from typing import Union

from .data_source import send_msg_to_mc, send_cmd_to_mc
from ...utils import msg_rule, permission_check

mc_qq = on_message(priority=2, rule=msg_rule)

mc_qq_cmd = on_command("minecraft_command", aliases={"mcc"}, priority=1, rule=msg_rule, block=True)

mc_qq_cmd.handle()(permission_check)


# 收到消息时
@mc_qq.handle()
async def msg_first_receive(bot: Bot, event: Union[GroupMessageEvent, GuildMessageEvent]):
    await send_msg_to_mc(bot=bot, event=event)


# 收到命令时
@mc_qq_cmd.handle()
async def cmd_first_receive(bot: Bot, event: Union[GroupMessageEvent, GuildMessageEvent], args: Message = CommandArg()):
    await send_cmd_to_mc(bot=bot, event=event, cmd=args.extract_plain_text())
