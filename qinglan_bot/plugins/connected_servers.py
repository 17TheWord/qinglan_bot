from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageEvent

from mcqq_tool.utils import CLIENTS
from ..utils import permission_check, to_me

connected_servers = on_command("已连接服务器列表", rule=to_me(), priority=3)
connected_servers.__doc__ = """已连接服务器列表（管理员）"""

connected_servers.handle()(permission_check)


@connected_servers.handle()
async def _(event: MessageEvent):
    """发送所有已连接至 WebSocket 的服务器"""
    message = "已连接至 WebSocket 的服务器列表\n\n"

    for server_name, server in CLIENTS.items():
        message += (
            f"{server_name} "
            f"WebSocket: {'开' if server.websocket else '关'}, "
            f"Rcon: {'开' if server.rcon else '关'}\n"
        )
    await connected_servers.finish(message=message)
