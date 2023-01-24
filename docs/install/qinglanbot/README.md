# 前提条件

::: warning 前提条件
青岚 Bot 基于 [NoneBot2](https://github.com/nonebot/nonebot2) 开发，因此依赖于 [Python](https://www.python.org/downloads/)。  
Python 版本请选择 Python3.9 / Python3.10（Python3.8 暂未测试）  
不会安装 Python 的可以参考 [廖雪峰的教程](https://www.liaoxuefeng.com/wiki/1016959663602400/1016959856222624)。
:::

::: danger 警告

[NoneBot2](https://github.com/nonebot/nonebot2) 与 [NoneBot](https://github.com/nonebot/nonebot) **不兼容且无法共存**！如果你曾经使用过 NoneBot 或基于 NoneBot 开发的机器人（如：[yobot](https://github.com/pcrbot/yobot)、[HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot)、[dd-bot](https://github.com/SK-415/dd-bot)），或者你不确定是否安装过 NoneBot。

那么在**开始安装之前**，请先尝试在终端（Powershell/cmd）内执行 `pip uninstall nonebot` **卸载** NoneBot，或者创建一个 [虚拟环境](https://docs.python.org/zh-cn/3/library/venv.html#creating-virtual-environments) 使 青岚 Bot 可以与 NoneBot 共存。
:::

---

如果你的 `Python` 基础较为薄弱，推荐使用 [脚手架安装](pip)
