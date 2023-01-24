from nonebot import on_command
from nonebot.adapters.onebot.v11.event import MessageEvent
from nonebot.params import ArgPlainText

from ..rcon import change_rcon_status
from ...database import DB as db
from ...utils import permission_check, handle_server_name, server_name_check, to_me

rcon_msg_off = on_command("关闭rcon消息", rule=to_me(), priority=3)
rcon_msg_off.__doc__ = """关闭rcon消息 Server（管理员）"""

rcon_msg_off.handle()(permission_check)

rcon_msg_off.handle()(handle_server_name)

rcon_msg_off.got("server_name", prompt="请输入要关闭 Rcon_Msg 的服务器")(server_name_check)


@rcon_msg_off.handle()
async def _(event: MessageEvent, server_name: str = ArgPlainText("server_name")):
    """根据 服务器名 开启 Rcon_Msg"""
    if await db.update_server(
            "rcon_msg",
            False,
            server_name=server_name,
    ):
        await change_rcon_status(server_name=server_name)
        server = await db.get_server(server_name=server_name)
        assert server is not None
        await rcon_msg_off.finish(f"已关闭 [{server.server_name}] 的Rcon_Msg")
    await rcon_msg_off.finish(f"服务器（{server_name}）未互通，请先互通后再操作")
