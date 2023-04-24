import aiomcrcon
from nonebot import logger
from mcqq_tool.utils import get_client, rcon_connect

from . import change_ip, change_port, change_password
from ...database.db import DB as db, server_list


async def change_rcon_status(server_name):
    """更新Rcon状态"""
    for server in server_list:
        if (client := get_client(server_name=server_name)) and server.server_name == server_name:
            # 获取该服务器的信息
            server = await db.get_server(server_name=server_name)
            # 开
            if server.rcon_msg or server.rcon_cmd and not client.rcon:
                client.rcon = aiomcrcon.Client(
                    server.rcon_ip,
                    server.rcon_port,
                    server.rcon_password
                )
                await rcon_connect(rcon_client=client.rcon, server_name=server_name)

            # 关：rcon消息关、rcon命令关、rcon状态开
            if not server.rcon_msg and not server.rcon_cmd and client.rcon:
                await client.rcon.close()
                logger.success(f"[MC_QQ]丨[Server:{server.server_name}] 的Rcon已关闭")
