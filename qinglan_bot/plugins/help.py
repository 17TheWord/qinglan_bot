from nonebot import on_command
from nonebot.matcher import matchers

from ..utils import to_me

help = on_command("ql帮助", rule=to_me(), priority=3)


@help.handle()
async def _():
    message = "青岚 目前支持的功能：\n（请将Server替换为需要操作的服务器名）\n"
    for matchers_list in matchers.values():
        for matcher in matchers_list:
            if (
                    matcher.plugin_name
                    and matcher.plugin_name.startswith("qinglan_bot")
                    and matcher.__doc__
            ):
                message += matcher.__doc__ + "\n"
    message += "详细帮助：https://17theword.github.io/qinglan_bot"
    await help.finish(message)
