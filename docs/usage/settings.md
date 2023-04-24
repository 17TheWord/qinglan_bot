# 进阶设置

- 这里涉及到了有关 NoneBot 配置文件的相关配置

- 这些配置并非必须项，如有需求可自行修改

- 不填写的话，将采用默认值

::: details 示例（点我展开）

```json {7-8}
HOST=0.0.0.0
PORT=8080
SUPERUSERS=[]
NICKNAME=[]
COMMAND_START=[""]

MC_QQ_DIR="./data/"
mc_qq_to_me=false
mc_qq_guild_admin_roles=["MCQQ", "频道主"]
```

:::

## WebSocket 地址

默认值：`"127.0.0.1"`

- WebSocket服务器 IP

  ```json {7-8}
  mc_qq_ws_ip = "127.0.0.1"
  ```

## WebSocket 端口

默认值：`8765`

- WebSocket服务器 端口

  ```json {7-8}
  mc_qq_ws_port = 8765
  ```

## 数据库路径

默认值：`"./data/"`

- MCQQ Bot 存储数据库的路径，数据库名为 `mcqq.sqlite3`

  ```json {7-8}
  mc_qq_dir = "./data/"
  ```

## 是否启用 `@`

默认值：`true`

- 在使用命令时，是否需要 `@MCQQ Bot`

  ```json {7-8}
  mc_qq_to_me = false
  ```


## 频道管理员身份组

默认值：`["频道主", "超级管理员"]`

- 频道中可以使用发送有效命令的身份组

  ```json {7-8}
  mc_qq_guild_admin_roles = ["管理员", "服务器OP"]
  ```



