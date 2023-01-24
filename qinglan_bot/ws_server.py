import websockets
from nonebot import logger

from .plugins.on_msg.data_source import ws_client
from .utils import config


async def start_ws_server():
    """启动 WebSocket 服务器"""
    global ws
    ws = await websockets.serve(ws_client, config.get_mc_qq_ws_ip(), config.get_mc_qq_ws_port())
    logger.success("[MC_QQ]丨WebSocket 服务器已开启")


async def stop_ws_server():
    """关闭 WebSocket 服务器"""
    global ws
    ws.close()
    logger.success("[MC_QQ]丨WebSocket 服务器已关闭")
