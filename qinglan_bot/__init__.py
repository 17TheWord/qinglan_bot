from nonebot import get_driver
from nonebot.plugin.manager import PluginLoader
from .config import Config

if isinstance(globals()["__loader__"], PluginLoader):
    driver = get_driver()

    plugin_config: Config = Config.parse_obj(get_driver().config)

    from .ws_server import start_ws_server, stop_ws_server
    from . import plugins

    # Bot 连接时
    @driver.on_bot_connect
    async def on_start():
        # 启动 WebSocket 服务器
        await start_ws_server()

    # Bot 断开时
    @driver.on_bot_disconnect
    async def on_close():
        # 关闭 WebSocket 服务器
        await stop_ws_server()
