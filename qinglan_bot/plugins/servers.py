from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageEvent

from ..database.models import Server
from ..utils import permission_check, to_me

servers = on_command("服务器列表", rule=to_me(), priority=3)

servers.handle()(permission_check)


@servers.handle()
async def _(event: MessageEvent):
    """发送数据库中所有服务器"""
    message = "数据库中的服务器列表\n\n"
    server_list = Server.all()
    async for server in server_list:
        message += (
            f"{server.server_name} "
            f"Rcon_Msg：{'开' if server.rcon_msg else '关'}，"
            f"Rcon_CMD：{'开' if server.rcon_cmd else '关'}，"
        )
    await servers.finish(message=message)
