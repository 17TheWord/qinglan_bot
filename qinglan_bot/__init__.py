from nonebot import get_driver, ReverseDriver
from nonebot.plugin import PluginMetadata
from nonebot.plugin.manager import PluginLoader
from .config import Config

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

    from .router import set_route
    from . import plugins

    # Bot 连接时
    @driver.on_startup
    async def on_start():
        # 启动 WebSocket 服务器
        if isinstance(driver, ReverseDriver):
            await set_route(driver=driver)
