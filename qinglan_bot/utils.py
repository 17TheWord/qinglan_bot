import json
from typing import Union

from mcqq_tool.utils import get_member_nickname
from nonebot.adapters.onebot.v11 import Message, GroupMessageEvent, Bot, GROUP_ADMIN, GROUP_OWNER, PrivateMessageEvent
from nonebot.exception import FinishedException
from nonebot.internal.permission import Permission
from nonebot.internal.rule import Rule
from nonebot.matcher import Matcher
from nonebot.params import ArgPlainText, CommandArg
from nonebot.permission import SUPERUSER
from nonebot_plugin_guild_patch import ChannelDestroyedNoticeEvent, GuildMessageEvent

from . import plugin_config
from .database.db import rule_group_list, rule_guild_list


def to_me():
    if plugin_config.mc_qq_to_me:
        from nonebot.rule import to_me

        return to_me()

    async def _to_me() -> bool:
        return True

    return Rule(_to_me)


async def _guild_admin(bot: Bot, event: GuildMessageEvent):
    roles = set(
        role["role_name"]
        for role in (
            await bot.get_guild_member_profile(
                guild_id=event.guild_id, user_id=event.user_id
            )
        )["roles"]
    )
    return bool(roles & set(plugin_config.mc_qq_guild_admin_roles))


GUILD_ADMIN: Permission = Permission(_guild_admin)


async def permission_check(
        bot: Bot, event: Union[GroupMessageEvent, GuildMessageEvent, PrivateMessageEvent]
):
    # from ..database import DB as db

    if isinstance(event, PrivateMessageEvent):
        if event.sub_type == "group":  # 不处理群临时会话
            raise FinishedException
        if await SUPERUSER(bot, event):
            return

    if isinstance(event, GroupMessageEvent):
        # if not await db.get_group_admin(event.group_id):
        #     return
        if await (GROUP_ADMIN | GROUP_OWNER | SUPERUSER)(bot, event):
            return
    elif isinstance(event, GuildMessageEvent):
        # if not await db.get_guild_admin(event.guild_id, event.channel_id):
        #     return
        if await (GUILD_ADMIN | SUPERUSER)(bot, event):
            return
    await bot.send(event, "权限不足，目前只有管理员才能使用")
    raise FinishedException


async def handle_server_name(
        matcher: Matcher,
        command_arg: Message = CommandArg(),
):
    server_name = command_arg.extract_plain_text().strip()
    if server_name:
        matcher.set_arg("server_name", command_arg)


async def server_name_check(
        matcher: Matcher,
        server_name: str = ArgPlainText("server_name"),
):
    server_name = server_name.strip()
    matcher.set_arg("server_name", Message(server_name))


async def get_type_id(event: Union[GroupMessageEvent, GuildMessageEvent, ChannelDestroyedNoticeEvent]):
    if isinstance(event, GuildMessageEvent) or isinstance(event, ChannelDestroyedNoticeEvent):
        from .database import DB as db
        return await db.get_guild_type_id(event.guild_id, event.channel_id)
    return event.group_id


async def msg_rule(event: Union[GroupMessageEvent, GuildMessageEvent]) -> bool:
    """Rule 消息规则"""
    if isinstance(event, GroupMessageEvent):
        return event.group_id in rule_group_list
    elif isinstance(event, GuildMessageEvent):
        return f"{event.guild_id}:{event.channel_id}" in rule_guild_list
    return False


async def process_msg_for_ws(bot: Bot, event: Union[GroupMessageEvent, GuildMessageEvent]):
    """处理发送至MC的信息"""
    # 获取昵称
    member_nickname = await get_member_nickname(bot, event, event.user_id)

    # 初始化消息
    text_msg = member_nickname + "说："

    # 初始化消息字典
    messageList = []

    # 发送群聊名称
    from .database import DB as db
    if isinstance(event, GroupMessageEvent) and (await db.get_group(group_id=event.group_id)).send_group_name:
        group_name = {'msgType': "group_name",
                      'msgData': (await bot.get_group_info(group_id=event.group_id))['group_name']}
        messageList.append(group_name)
    elif isinstance(event, GuildMessageEvent) and (
            await db.get_guild(guild_id=event.guild_id, channel_id=event.channel_id)).send_group_name:
        group_name = {'msgType': "group_name"}
        guild_name = (await bot.get_guild_meta_by_guest(guild_id=event.guild_id))['guild_name']
        for per_channel in (await bot.get_guild_channel_list(guild_id=event.guild_id, no_cache=True)):
            if str(event.channel_id) == per_channel['channel_id']:
                channel_name = per_channel['channel_name']
                group_name['msgData'] = f"{guild_name}丨{channel_name}"
                break
        messageList.append(group_name)

    # 将群成员昵称装入消息列表
    messageList.append({"msgType": "senderName", "msgData": member_nickname})

    for msg in event.message:
        per_msg = {'msgType': msg.type}
        # 文本
        if msg.type == "text":
            msgData = msg.data['text'].replace("\r", "").replace("\n", "\n * ")
            text_msg += msgData
        # 图片
        elif msg.type == "image":
            msgData = msg.data['url']
            text_msg += '[图片]'
        # 表情
        elif msg.type == "face":
            msgData = '[表情]'
            text_msg += '[表情]'
        # 语音
        elif msg.type == "record":
            msgData = '[语音]'
            text_msg += '[语音]'
        # 视频
        elif msg.type == "video":
            msgData = msg.data['url']
            text_msg += '[视频]'
        # @
        elif msg.type == "at":
            # 获取被@ 群/频道 昵称
            at_member_nickname = await get_member_nickname(bot, event, msg.data['qq'])
            msgData = f"@{at_member_nickname}"
            text_msg += msgData
        # share
        elif msg.type == "share":
            msgData = msg.data['url']
            text_msg += '[分享：' + msg.data['title'] + ']'
        # forward
        elif msg.type == "forward":
            # TODO 将合并转发消息拼接为字符串
            # 获取合并转发 await bot.get_forward_msg(message_id=event.message_id)
            msgData = '[合并转发]'
            text_msg = msgData
        else:
            msgData = msg.type
            text_msg += '[' + msg.type + '] '

        text_msg += " "

        # 装入消息数据
        per_msg['msgData'] = msgData
        # 放入消息列表
        messageList.append(per_msg)

    return text_msg, str({"message": messageList})


async def process_msg_for_rcon(bot: Bot, event: Union[GroupMessageEvent, GuildMessageEvent]):
    """消息处理"""
    # 获取昵称
    member_nickname = await get_member_nickname(bot, event, event.user_id)

    # 初始化日志消息
    text_msg = member_nickname + " 说："

    command_msg = "tellraw @p "

    message_list = [
        {"text": "[MC_QQ] ", "color": "yellow"},
    ]
    # 是否发送群聊名称
    from .database import DB as db
    # 群
    if isinstance(event, GroupMessageEvent) and (await db.get_group(group_id=event.group_id)).send_group_name:
        message_list.append(
            {"text": (await bot.get_group_info(group_id=event.group_id))['group_name'] + " ", "color": "aqua"})
    # 频道
    elif isinstance(event, GuildMessageEvent) and (
            await db.get_guild(guild_id=event.guild_id, channel_id=event.channel_id)).send_group_name:
        guild_name = (await bot.get_guild_meta_by_guest(guild_id=event.guild_id))['guild_name']
        for per_channel in (await bot.get_guild_channel_list(guild_id=event.guild_id, no_cache=True)):
            if str(event.channel_id) == per_channel['channel_id']:
                message_list.append({"text": guild_name + "丨" + per_channel['channel_name'] + " ", "color": "aqua"})
                break
    message_list.append({"text": member_nickname, "color": "aqua"})
    message_list.append({"text": " 说：", "color": "yellow"})

    for msg in event.message:
        # 文本
        if msg.type == "text":
            msg_dict = {"text": msg.data['text'].replace("\r", "").replace("\n", "\n * ") + " ", "color": "white"}
            text_msg += msg.data['text'].replace("\r", "").replace("\n", "\n * ")
        # 图片
        elif msg.type == "image":
            msg_dict = {"text": "[图片] ", "color": "yellow",
                        "clickEvent": {"action": "open_url", "value": msg.data['url']},
                        "hoverEvent": {"action": "show_text", "contents": [{"text": "查看图片", "color": "gold"}]}
                        }
            text_msg += '[图片]'
        # 表情
        elif msg.type == "face":
            msg_dict = {"text": "[表情] ", "color": "gold"}
            text_msg += '[表情]'
        # 语音
        elif msg.type == "record":
            msg_dict = {"text": "[语音] ", "color": "light_purple"}
            text_msg += '[语音]'
        # 视频
        elif msg.type == "video":
            msg_dict = {"text": "[视频] ", "color": "light_purple",
                        "clickEvent": {"action": "open_url", "value": msg.data['url']},
                        "hoverEvent": {"action": "show_text", "contents": [{"text": "查看视频", "color": "dark_purple"}]}
                        }
            text_msg += '[视频]'
        # @
        elif msg.type == "at":
            # 获取被@ 群/频道 昵称
            at_member_nickname = await get_member_nickname(bot, event, msg.data['qq'])
            msg_dict = {"text": "@" + at_member_nickname + " ", "color": "green"}
            text_msg += f"@{at_member_nickname}"
        # share
        elif msg.type == "share":
            msg_dict = {"text": "[分享：" + msg.data['title'] + "] ", "color": "yellow",
                        "clickEvent": {"action": "open_url", "value": msg.data['url']},
                        "hoverEvent": {"action": "show_text", "contents": [{"text": "查看图片", "color": "gold"}]}
                        }
            text_msg += '[分享：' + msg.data['title'] + ']'
        # forward
        elif msg.type == "forward":
            # TODO 将合并转发消息拼接为字符串
            # 获取合并转发 await bot.get_forward_msg(message_id=event.message_id)
            msg_dict = {"text": "[合并转发] ", "color": "white"}
            text_msg += '[合并转发]'
        else:
            msg_dict = {"text": "[ " + msg.type + "] ", "color": "white"}
            text_msg += '[' + msg.type + ']'

        # 放入消息列表
        message_list.append(msg_dict)

    # 拼接完整命令
    command_msg += json.dumps(message_list)
    return text_msg, command_msg
