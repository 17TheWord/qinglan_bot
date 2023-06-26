from nonebot import get_driver, require
from nonebot.plugin import PluginMetadata
from nonebot.plugin.manager import PluginLoader
from .config import Config

require("nonebot_plugin_guild_patch")

__plugin_meta__ = PluginMetadata(
    name="青岚Bot",
    description="基于NoneBot的与Minecraft Server互通消息的机器人",
    homepage="https://github.com/17TheWord/qinglan_bot",
    usage="配置完成后在群聊发送消息即可同步至 Minecraft 服务器",
    config=Config,
    type="application",
    supported_adapters={
        "nonebot.adapters.onebot.v11"
    }
)
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
