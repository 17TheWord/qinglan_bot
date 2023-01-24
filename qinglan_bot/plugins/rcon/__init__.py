import aiomcrcon
from nonebot import logger

from . import change_ip, change_port, change_password
from ..on_msg.data_source import CLIENTS, rcon_connect
from ...database import DB as db


async def change_rcon_status(server_name):
    """更新Rcon状态"""
    for client in CLIENTS:
        # 如果服务器名匹配
        if client["server_name"] == server_name:
            # 获取该服务器的信息
            server = await db.get_server(server_name=server_name)
            # 开
            if server.rcon_msg or server.rcon_cmd and not client["rcon_connection"]["is_open"]:
                client["rcon_connection"]["rcon"] = aiomcrcon.Client(
                    server.rcon_ip,
                    server.rcon_port,
                    server.rcon_password
                )
                await rcon_connect(client=client["rcon_connection"]["rcon"], server_name=server_name)

            # 关：rcon消息关、rcon命令关、rcon状态开
            if not server.rcon_msg and not server.rcon_cmd and client["rcon_connection"]["is_open"]:
                await client["rcon_connection"]["rcon"].close()
                client["rcon_connection"]["is_open"] = False
                logger.success(f"[MC_QQ]丨[Server:{server.server_name}] 的Rcon已关闭")
