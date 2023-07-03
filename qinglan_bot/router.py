from typing import Optional

from aiomcrcon import Client as RconClient

from mcqq_tool.config import CLIENTS, Client
from mcqq_tool.common import plugin_config
from mcqq_tool.utils import send_msg_to_qq, remove_client, rcon_connect

from nonebot import get_bot, logger
from nonebot.exception import WebSocketClosed
from nonebot.drivers import URL, ReverseDriver, WebSocket, WebSocketServerSetup


async def _ws_handler(websocket: WebSocket):
    """WebSocket"""
    try:
        server_name = websocket.request.headers.get("x-self-name").encode('utf-8').decode('unicode_escape')
    except KeyError as e:
        # 服务器名为空
        logger.error(f"[MC_QQ]丨未获取到该服务器的名称，连接断开：{e}")
        await websocket.close(1008, "[MC_QQ]丨未获取到该服务器的名称，连接断开")
        return
    else:

        if CLIENTS.get(server_name):
            # 服务器名已存在
            logger.error(f"[MC_QQ]丨已有相同服务器名的连接，连接断开")
            await websocket.close(1008, "[MC_QQ]丨已有相同服务器名的连接")
            return

        # 准备加入客户端列表
        from .database import DB as db
        rcon_client: Optional[RconClient] = None
        bot_self_id = None
        if server := await db.get_server(server_name=server_name):
            # rcon状态：rcon_msg rcon_cmd rcon_password不等于默认密码
            if (server.rcon_msg or server.rcon_cmd) and server.rcon_password != "change_password":
                bot_self_id = str(server.bot_self_id) if server.bot_self_id else None
                rcon_client = RconClient(server.rcon_ip, server.rcon_port, server.rcon_password)
                await rcon_connect(rcon_client=rcon_client, server_name=server_name)

        CLIENTS[server_name] = Client(server_name=server_name, websocket=websocket, rcon=rcon_client)

        await websocket.accept()

        logger.success(f"[MC_QQ]丨[Server:{server_name}] 已连接至 WebSocket 服务器")

        try:
            while True:
                try:
                    message = await websocket.receive()
                    # 获取指定ID Bot
                    bot = get_bot(bot_self_id)
                except KeyError as e:
                    logger.warning(f"[MC_QQ]丨[Server:{server_name}] 对应 self_id 的 Bot 不存在：{e}")
                except ValueError as e:
                    logger.warning(f"[MC_QQ]丨[Server:{server_name}] 未指定Bot，且当前无其他Bot可用：{e}")
                else:
                    # 以指定ID Bot 发送消息
                    await send_msg_to_qq(bot=bot, message=message)
        except WebSocketClosed as e:
            logger.warning(f"[MC_QQ]丨[Server:{server_name}] 的 WebSocket 出现异常：{e}")
        finally:
            await remove_client(server_name=server_name)


async def set_route(driver: ReverseDriver):
    driver.setup_websocket_server(
        WebSocketServerSetup(
            path=URL(plugin_config.mc_qq_ws_url),
            name="mcqq",
            handle_func=_ws_handler,
        )
    )
