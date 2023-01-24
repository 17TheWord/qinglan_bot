# 功能列表

::: warning 注意
群里使用命令前**需要** @机器人，如 `@青岚Bot ql帮助`。

如果**不希望**在使用命令前 @机器人，请查看 [进阶配置](./settings)。
:::

---

## 帮助

- 命令：`ql帮助`
- 获取目前 青岚 Bot 支持的所有功能指令。

::: tip 提示
功能表会随版本变化，请以自己机器人帮助信息为准。
:::

## 互通列表

- 命令：`互通列表`
- 场景：`群聊丨管理员`
- 描述：获取当前 `群聊丨子频道` 所互通的服务器列表。

## 已连接服务器列表

- 命令：`已连接服务器列表`
- 场景：`管理员`
- 描述：获取已经连接至 `WebSocket` 的所有服务器。

## 服务器列表

- 命令：`服务器列表`
- 场景：`管理员`
- 描述：获取数据库中已经记录的服务器列表。

## 互通

- 命令：`开启互通 ServerName`丨`关闭互通 ServerName`
- 场景：`群聊丨管理员`
- 描述：当前群聊与名为 `ServerName` 的服务器互通。

## 是否发送群名

- 命令：`开启发送群名`丨`关闭发送群名`
- 场景：`群聊丨管理员`
- 描述：当前群聊名称随着群员消息一并发送至MC，并显示在群员昵称之前。

## 是否发送服务器名

- 命令：`开启服务器名 ServerName`丨`关闭服务器名 ServerName`
- 场景：`管理员`
- 描述：名为 `ServerName` 的服务器发送至群的消息中，添加服务器名称前缀 `[ServerName]`。

## Rcon消息

- 命令：`开启rcon消息 ServerName`丨`关闭rcon消息 ServerName`
- 场景：`管理员`
- 描述：发送至 `ServerName` 的消息采用 `Rcon` 发送，适用于支持Rcon的**非插件服务端**。

## Rcon命令

- 命令：`开启rcon命令 ServerName`丨`关闭rcon命令 ServerName`
- 场景：`管理员`
- 描述：发送至 `ServerName` 的命令采用 `Rcon` 发送，适用于所有支持Rcon的服务端。
- 使用：
  - 开启后，发送 `/mcc give player1 apple 1` 将会给予玩家 `player1` 一个苹果
  - 其中 `/` 为nb配置中的命令头

## 修改 Rcon IP

- 命令：`修改rconip ServerName ip`
- 场景：`私聊丨超级用户`
- 描述：修改名为 `ServerName` 服务器的 Rcon IP。
- 使用：
  - 发送 `修改rconip server1 localhost` 会将名为 `server1` 服务器的 `Rcon_IP` 改为 `localhost`
- 注意：
  - 所有开启互通的服务器默认 RconIP 均为 `127.0.0.1`
  - 若有远程服务器，请自行修改

## 修改 Rcon 端口

- 命令：`修改rcon端口 ServerName port`
- 场景：`私聊丨超级用户`
- 描述：修改名为 `ServerName` 服务器的 Rcon 端口。
- 使用：
  - 发送 `修改rcon端口 server1 25576` 会将名为 `server1` 服务器的 `Rcon_Port` 改为 `25576`
- 注意：
  - 所有开启互通的服务器默认 Rcon端口 均为 `25575`
  - 若有多个服务器使用Rcon连接，请务必修改成不同的端口

## 修改 Rcon 密码

- 命令：`修改rcon密码 ServerName password`
- 场景：`私聊丨超级用户`
- 描述：修改名为 `ServerName` 服务器的 Rcon 密码。
- 使用：发送 `修改rcon密码 server1 123456789` 会将名为 `server1` 服务器的 `Rcon_PassWord` 改为 `123456789`
- 注意：
  - 所有开启互通的服务器默认 Rcon密码 均为 `change_password`
  - 若要使用 Rcon 请务必在使用前修改密码，并确保与服务器端一致，否则不会进行连接
