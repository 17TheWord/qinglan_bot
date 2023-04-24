import sys
import importlib
import nonebot

from os import path
from nonebot.adapters.onebot.v11 import Adapter
from nonebot.log import default_format, logger

nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter(Adapter)
app = nonebot.get_asgi()

# 删除 qinglan_bot 导入，否则 nonebot 导入时会忽略
del sys.modules["qinglan_bot"]
nonebot.load_plugin("qinglan_bot")

tqdm_loader = importlib.util.find_spec("nonebot_plugin_gocqhttp")
if tqdm_loader:
    nonebot.load_plugin("nonebot_plugin_gocqhttp")
else:
    nonebot.logger.info("未找到 nonebot_plugin_gocqhttp 包，请使用go-cqhttp独立连接程序")

# Modify some config / config depends on loaded configs
#
# config = nonebot.get_driver().config
# do something...

logger.add(
    path.join("log", "error.log"),
    rotation="00:00",
    retention="1 week",
    diagnose=False,
    level="ERROR",
    format=default_format,
    encoding="utf-8",
)


def run():
    nonebot.run(app="qinglan_bot.cli.bot:app")
