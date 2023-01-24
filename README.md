# 青岚Bot

基于NoneBot的与Minecraft Server互通消息的机器人

## 介绍

命名的灵感来自于我的一位朋友

在原插件上加入了动态配置的功能

数据库参考 [`HarukaBot`](https://github.com/SK-415/HarukaBot)

## 安装

- 文档：[仍在更新的青岚Bot文档](https://17theword.github.io/qinglan_bot/)

- NoneBot2
    - `pip install qinglan-bot`

    - 空目录下使用命令 `ql run`

- MineCraft Server
  - 前往 [插件Releases](https://github.com/17TheWord/nonebot-plugin-mcqq/releases) 下载对应服务端的 `jar` 文件并安装
  - `jar` 安装文档可参考 [MC_QQ](https://17theword.github.io/mc_qq/)

## 命令

- 帮助
    - 为防止与其他插件冲突
    - 请使用 `ql帮助` 来获取帮助


- 获取已连接至 WebSocket 的 MineCraft服务器
    - `服务器列表`


- 动态控制需要互通的群聊
    - `开启互通 Server1`
    - `开启互通 Server2`
    - `关闭互通 Server1`
    - `关闭互通 Server2`


- 获取当前群聊开启互通的服务器
    - `互通列表`


- 为当前群聊设置是否在发送消息到MC时携带群聊名称
    - `开启发送群名`
    - `关闭发送群名`


- 服务器在发送消息至群聊时，是否携带服务器名
    - `开启服务器名`
    - `关闭服务器名`


- 服务器是否启用Rcon来发送消息或命令
    - Rcon发送 消息和命令 适用于非插件端服务器
    - Rcon发送命令适用于纯插件端
    - `开启rcon消息 服务器名` 丨 `关闭rcon消息 服务器名`
    - `开启rcon命令 服务器名` 丨 `关闭rcon命令 服务器名`


- 修改服务器Rcon连接信息的IP、端口、密码
    - 为保障安全，仅限 `超级用户` 与 `Bot` 私聊使用
    - 为保障安全，若rcon密码为默认密码，将不会连接服务器的Rcon
    - `修改rconip 服务器名 新ip`
    - `修改rcon端口 服务器 新端口`
    - `修改rcon密码 服务器 新密码`


- 查看数据库中服务器列表
    - `服务器列表`


- 查看已经连接至 WebSocket 的服务器列表
    - `已连接服务器列表`

## 特别感谢

- [@SK-415](https://github.com/SK-415) ：感谢SK佬给予许多优秀的建议和耐心的解答。
- [@zhz-红石头](https://github.com/zhzhongshi) ：感谢红石头在代码上的帮助
- [SK-415/HarukaBot](https://github.com/SK-415/HarukaBot) ：感谢HarukaBot如此优雅的各类方法
- [NoneBot2](https://github.com/nonebot/nonebot2)： 插件使用的开发框架。
- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)： 稳定完善的 CQHTTP 实现。

## 贡献与支持

觉得好用可以给这个项目点个 `Star` 或者去 [爱发电](https://afdian.net/a/17TheWord) 投喂我。

有意见或者建议也欢迎提交 [Issues](https://github.com/17TheWord/qinglan_bot/issues)
和 [Pull requests](https://github.com/17TheWord/qinglan_bot/pulls)。

## 许可证

本项目使用 [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) 作为开源许可证。
