import json
import aiomcrcon
import websockets
from nonebot import get_bot, logger
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot_plugin_guild_patch import GuildMessageEvent

from typing import Union, Optional
from ...utils import process_msg_for_ws, send_msg_to_qq, get_type_id, process_msg_for_rcon
from ...database.db import server_list

CLIENTS = []
"""客户端列表"""


async def ws_client(websocket):
    """WebSocket"""
    try:
        server_name = websocket.request_headers["x-self-name"].encode('utf-8').decode('unicode_escape')
    except KeyError:
        server_name = ""
    # 服务器名为空
    if not server_name:
        logger.error("[MC_QQ]丨未获取到该服务器的名称，连接断开")
        await websocket.close(1008, "[MC_QQ]丨未获取到该服务器的名称，连接断开")
        return
    else:
        for client in CLIENTS:
            # 重复连接
            if server_name == client["server_name"]:
                logger.error(f"[MC_QQ]丨[Server:{server_name}] 已连接至 WebSocket 服务器，无需重复连接")
                await websocket.close(1008, f"[MC_QQ]丨[Server:{server_name}] 已连接至 WebSocket 服务器，无需重复连接")
                return
    # 准备加入客户端列表
    try:
        from ...database import DB as db
        server = await db.get_server(server_name=server_name)
        # rcon状态：rcon_msg rcon_cmd rcon_password不等于默认密码
        rcon_status = (server.rcon_msg or server.rcon_cmd) and server.rcon_password != "change_password"
    except AttributeError:
        rcon_status = False

    if rcon_status:
        rcon_client = aiomcrcon.Client(server.rcon_ip, server.rcon_port, server.rcon_password)
        await rcon_connect(client=rcon_client, server_name=server_name)
    else:
        rcon_client: Optional[aiomcrcon.Client] = None

    CLIENTS.append({
        "server_name": server_name, "ws_client": websocket, "rcon_connection": {
            "rcon": rcon_client, "is_open": rcon_status
        }
    })
    logger.success(f"[MC_QQ]丨[Server:{server_name}] 已连接至 WebSocket 服务器")
    try:
        async for message in websocket:
            await send_msg_to_qq(bot=get_bot(), json_msg=json.loads(message))
    except websockets.WebSocketException:
        # 移除当前客户端
        await remove_client(server_name)
    if websocket.closed and CLIENTS:
        await remove_client(server_name)


async def send_msg_to_mc(bot: Bot, event: Union[GroupMessageEvent, GuildMessageEvent]):
    """发送消息到 MC"""
    # 处理来自QQ的消息
    if client_list := await get_clients(event=event):
        for client in client_list:
            # 如果 服务器的rcon已连接 且 服务器切换为rcon发送消息
            if client["client"]["rcon_connection"]["is_open"] and client["server"]["rcon_msg"] and \
                    client["client"]["rcon_connection"]["rcon"]:
                text_msg, msgJson = await process_msg_for_rcon(bot=bot, event=event)
                try:
                    await client["client"]["rcon_connection"]["rcon"].send_cmd(msgJson)
                    logger.success(f"[MC_QQ_Rcon]丨发送至 [server:{client['client']['server_name']}] 的消息 \"{text_msg}\"")
                except aiomcrcon.ClientNotConnectedError:
                    logger.error(f"[MC_QQ]丨[Server:{client['client']['server_name']}] 的Rcon未连接，发送消息失败")

            elif client["client"]['ws_client']:
                text_msg, msgJson = await process_msg_for_ws(bot=bot, event=event)
                try:
                    await client["client"]['ws_client'].send(msgJson)
                    logger.success(f"[MC_QQ]丨发送至 [server:{client['client']['server_name']}] 的消息 \"{text_msg}\"")
                except websockets.WebSocketException:
                    logger.error(f"[MC_QQ]丨发送至 [Server:{client['client']['server_name']}] 的过程中出现了错误")
                    await remove_client(client['client']['server_name'])


async def send_command_to_mc(bot: Bot, event: Union[GroupMessageEvent, GuildMessageEvent]):
    """发送命令到 Minecraft"""
    if client_list := await get_clients(event=event):
        for client in client_list:
            if client["client"]["rcon_connection"]["is_open"] and client["server"]["rcon_cmd"] and \
                    client["client"]["rcon_connection"]["rcon"]:
                try:
                    await bot.send(event, message=str(
                        (await client["client"]["rcon_connection"]["rcon"].send_cmd(
                            event.raw_message.strip("/").strip("/mcc").strip()))[0]))
                    logger.success(
                        f"[MC_QQ_Rcon]丨发送至 [server:{client['client']['server_name']}] 的命令 \"{event.raw_message.strip('/mcc').strip()}\""
                    )
                except aiomcrcon.ClientNotConnectedError:
                    logger.error(f"[MC_QQ_Rcon]丨发送至 [Server:{client['client']['server_name']}] 的过程中出现了错误")
                    # 连接关闭则移除客户端
                    await remove_client(client['client']['server_name'])


async def get_clients(event: Union[GroupMessageEvent, GuildMessageEvent]):
    """获取 服务器名、ws客户端、rcon连接"""
    res = []
    for per_client in CLIENTS:
        for per_server in server_list:
            # 如果 服务器名 == ws客户端中记录的服务器名，且ws客户端存在
            if per_client['ws_client'] and per_server['server_name'] == per_client['server_name']:
                for per_group in per_server['all_group_list']:
                    if await get_type_id(event) == per_group["type_id"]:
                        res.append({"client": per_client, "server": per_server})
    return res


async def connect_rcon():
    """服务器启动时，连接启用rcon的服务器"""
    for server in server_list:
        if (server.rcon_msg | server.rcon_cmd) and server.rcon_password != "change_password":
            rcon_client = aiomcrcon.Client(server.rcon_ip, server.rcon_port, server.rcon_password)
            try:
                await rcon_client.connect()
                # 连接成功后装入rcon连接列表
                for client in CLIENTS:
                    if server.server_name == client["server_name"]:
                        client["rcon_connection"]["rcon"] = rcon_client
                        client["rcon_connection"]["is_open"] = True
                    logger.success(f"[MC_QQ]丨[Server:{client['server_name']}] 的Rcon连接成功")
            except aiomcrcon.RCONConnectionError:
                logger.error(f"[MC_QQ]丨[Server:{server.server_name}] 的Rcon连接失败")
            except aiomcrcon.IncorrectPasswordError:
                logger.error(f"[MC_QQ]丨[Server:{server.server_name}] 的Rcon密码错误")


async def rcon_connect(client: aiomcrcon.Client, server_name: str):
    """连接 Rcon"""
    try:
        await client.connect()
        logger.success(f"[MC_QQ]丨[Server:{server_name}] 的Rcon连接成功")
    except aiomcrcon.RCONConnectionError:
        logger.error(f"[MC_QQ]丨[Server:{server_name}] 的Rcon连接失败")
    except aiomcrcon.IncorrectPasswordError:
        logger.error(f"[MC_QQ]丨[Server:{server_name}] 的Rcon密码错误")


async def remove_client(server_name: str):
    """移除客户端"""
    for client in CLIENTS:
        if server_name == client["server_name"]:
            if client["rcon_connection"]["is_open"]:
                await client["rcon_connection"]["rcon"].close()
                logger.error(f"[MC_QQ]丨[Server:{server_name}] 的 Rcon 连接已断开")
            CLIENTS.remove(client)
            logger.error(f"[MC_QQ]丨[Server:{server_name}] 的 WebSocket 连接已断开")
