import aiomcrcon
import websockets
from typing import Optional, Union, List
from mcqq_tool.config import CLIENTS, Client
from mcqq_tool.utils import send_msg_to_qq, remove_client, rcon_connect, get_client
from nonebot import get_bot, logger
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot
from nonebot_plugin_guild_patch import GuildMessageEvent

from ...database.db import server_list, MinecraftServer
from ...utils import process_msg_for_ws, process_msg_for_rcon, get_type_id


async def ws_client(websocket: websockets.WebSocketServerProtocol):
    """WebSocket"""
    try:
        server_name = websocket.request_headers["x-self-name"].encode('utf-8').decode('unicode_escape')
    except KeyError as e:
        # 服务器名为空
        logger.error(f"[MC_QQ]丨未获取到该服务器的名称，连接断开：{e}")
        await websocket.close(1008, "[MC_QQ]丨未获取到该服务器的名称，连接断开")
        return
    else:
        try:
            client = CLIENTS[server_name]
        except KeyError as e:
            # 准备加入客户端列表
            from ...database import DB as db
            rcon_client: Optional[aiomcrcon.Client] = None
            if server := await db.get_server(server_name=server_name):
                # rcon状态：rcon_msg rcon_cmd rcon_password不等于默认密码
                if (server.rcon_msg or server.rcon_cmd) and server.rcon_password != "change_password":
                    rcon_client = aiomcrcon.Client(server.rcon_ip, server.rcon_port, server.rcon_password)
                    await rcon_connect(rcon_client=rcon_client, server_name=server_name)
            CLIENTS[server_name] = Client(server_name=server_name, websocket=websocket, rcon=rcon_client)
            logger.success(f"[MC_QQ]丨[Server:{server_name}] 已连接至 WebSocket 服务器")

            try:
                async for message in websocket:
                    await send_msg_to_qq(bot=get_bot(), message=message)
            except websockets.WebSocketException as e:
                # 移除当前客户端
                await remove_client(server_name=server_name)
                logger.error(f"[MC_QQ]丨[Server:{server_name}] 的 WebSocket 连接已断开：{e}")
            else:
                if websocket.closed:
                    await remove_client(server_name=server_name)
                    logger.error(f"[MC_QQ]丨[Server:{server_name}] 的 WebSocket 连接已断开")
        else:
            logger.error(f"[MC_QQ]丨[Server:{server_name}] 重复连接，连接断开")
            await websocket.close(1008, f"[MC_QQ]丨[Server:{server_name}] 重复连接，连接断开")


async def send_msg_to_mc(bot: Bot, event: Union[GroupMessageEvent, GuildMessageEvent]):
    """发送消息到 MC"""
    # 处理来自QQ的消息
    if client_list := await get_clients(event=event):
        for client_server in client_list:
            client = CLIENTS.get(client_server.server_name)
            # 如果 服务器的rcon已连接 且 服务器切换为rcon发送消息
            if client.rcon and client_server.rcon_msg:
                text_msg, msgJson = await process_msg_for_rcon(bot=bot, event=event)
                try:
                    await client.rcon.send_cmd(msgJson)
                except aiomcrcon.ClientNotConnectedError:
                    logger.error(f"[MC_QQ]丨[Server:{client.server_name}] 的Rcon未连接，发送消息失败")
                else:
                    logger.success(f"[MC_QQ_Rcon]丨发送至 [server:{client.server_name}] 的消息 \"{text_msg}\"")

            elif client.websocket:
                text_msg, msgJson = await process_msg_for_ws(bot=bot, event=event)
                try:
                    await client.websocket.send(msgJson)
                except websockets.WebSocketException:
                    logger.error(f"[MC_QQ]丨发送至 [Server:{client.server_name}] 的过程中出现了错误")
                    await remove_client(client.server_name)
                else:
                    logger.success(f"[MC_QQ]丨发送至 [server:{client.server_name}] 的消息 \"{text_msg}\"")


async def send_cmd_to_mc(bot: Bot, event: Union[GroupMessageEvent, GuildMessageEvent], cmd: str):
    """发送命令到 Minecraft"""
    if client_list := await get_clients(event=event):
        for client_server in client_list:
            client = CLIENTS.get(client_server.server_name)

            if client.rcon and client_server.rcon_cmd:
                # 获取命令
                try:
                    # 发送命令并获得返回消息
                    back_msg = await client.rcon.send_cmd(cmd)
                    # 机器人发送信息
                    await bot.send(event, message=back_msg[0])
                except aiomcrcon.ClientNotConnectedError:
                    # 连接关闭则移除客户端
                    await remove_client(client.server_name)
                    logger.error(f"[MC_QQ_Rcon]丨发送至 [Server:{client.server_name}] 的过程中出现了错误")
                else:
                    logger.success(f"[MC_QQ_Rcon]丨发送至 [server:{client.server_name}] 的命令 \"{cmd}\"")


async def get_clients(event: Union[GroupMessageEvent, GuildMessageEvent]) -> List[MinecraftServer]:
    """获取 服务器名、ws客户端、rcon连接"""
    res: List[MinecraftServer] = []
    for per_server in server_list:
        if client := get_client(per_server.server_name):
            if client.websocket and client.server_name == per_server.server_name:
                for per_group in per_server.all_group_list:
                    if await get_type_id(event) == per_group.type_id:
                        res.append(per_server)
    return res
