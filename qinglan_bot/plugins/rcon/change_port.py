from nonebot import on_command
from nonebot.params import ArgPlainText
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import PrivateMessageEvent
from ...database import DB as db
from ...utils import handle_server_name, server_name_check, to_me

change_ip = on_command("修改rcon端口", rule=to_me(), permission=SUPERUSER, priority=3)
change_ip.__doc__ = """修改rcon端口 Server PORT（私聊丨超级用户）"""

change_ip.handle()(handle_server_name)

change_ip.got("server_name", prompt="请输入内容：服务器名 PORT")(server_name_check)


@change_ip.handle()
async def _(event: PrivateMessageEvent, server_name: str = ArgPlainText("server_name")):
    """根据服务器名 修改 服务器PORT"""
    if event.sub_type != "group":  # 不处理群临时会话
        arg_list = server_name.split()
        if await db.update_server(
                "rcon_port",
                arg_list[1],
                server_name=arg_list[0],
        ):
            server = await db.get_server(server_name=arg_list[0])
            assert server is not None
            await change_ip.finish(f"修改 [{server.server_name}] 的Rcon_PORT成功")
        await change_ip.finish(f"服务器（{arg_list[0]}）未互通，请先互通后再操作")
