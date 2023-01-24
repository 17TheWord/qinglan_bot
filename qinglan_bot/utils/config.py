from nonebot import get_driver


def get_mc_qq_ws_ip() -> str:
    """获取 WebSocket IP"""
    try:
        return str(get_driver().config.mc_qq_ws_ip)
    except AttributeError:
        return "localhost"


def get_mc_qq_ws_port() -> int:
    """获取 WebSocket 端口"""
    try:
        return int(get_driver().config.mc_qq_ws_port)
    except AttributeError:
        return 8765


def get_mc_qq_send_group_name() -> bool:
    """获取 是否发送群聊名称"""
    try:
        return bool(get_driver().config.mc_qq_send_group_name)
    except AttributeError:
        return False


def get_mc_qq_display_server_name() -> bool:
    """获取 是否显示服务器名称"""
    try:
        return bool(get_driver().config.mc_qq_display_server_name)
    except AttributeError:
        return False


def get_mc_qq_servers_list() -> list:
    """获取 服务器列表"""
    try:
        return list(get_driver().config.mc_qq_servers_list)
    except AttributeError:
        return []


def get_mc_qq_mcrcon_guild_admin_roles() -> list:
    """获取频道 MC_QQ 管理身份组"""
    try:
        return list(get_driver().config.mc_qq_mcrcon_guild_admin_roles)
    except AttributeError:
        return ["频道主", "管理员"]


def get_mc_qq_dir() -> str:
    """获取 MC_QQ 数据库路径"""
    try:
        return str(get_driver().config.mc_qq_dir)
    except AttributeError:
        return ""


def get_mc_qq_to_me() -> bool:
    """获取 MC_QQ 数据库路径"""
    try:
        return bool(get_driver().config.mc_qq_to_me)
    except AttributeError:
        return True
