# 进阶设置

这里涉及到了有关 NoneBot 配置文件的相关配置

这些配置并非必须项，如有需求可自行修改

::: details 示例（点我展开）

```json {7-8}
HOST=0.0.0.0
PORT=8080
SUPERUSERS=[]
NICKNAME=[]
COMMAND_START=[""]

MC_QQ_DIR="./data/"
MC_QQ_TO_ME=false
MC_QQ_MCRCON_GUILD_ADMIN_ROLES=["MCQQ", "频道主"]
```

:::

## WebSocket 地址

默认值：`"127.0.0.1"`

- WebSocket服务器 IP

  ```json {7-8}
  MC_QQ_IP="127.0.0.1"
  ```

## WebSocket 端口

默认值：`8765`

- WebSocket服务器 端口

  ```json {7-8}
  MC_QQ_WS_PORT=8765
  ```

## 数据库路径

默认值：`"./data/"`

- MCQQ Bot 存储数据库的路径，数据库名为 `mcqq.sqlite3`

  ```json {7-8}
  MC_QQ_DIR="./data/"
  ```

## 是否启用 `@`

默认值：`true`

- 在使用命令时，是否需要 `@MCQQ Bot`

  ```json {7-8}
  MC_QQ_TO_ME=false
  ```


## 频道管理员身份组

默认值：`["频道主", "管理员"]`

- 频道中可以使用发送有效命令的身份组
  - NoneBot 读取配置文件为按行读取，填写后请将他们缩减为一行，如上方示例一样

  ```json {7-8}
  MC_QQ_MCRCON_GUILD_ADMIN_ROLES=[
    "管理员",
    "服务器OP"
  ]
  ```



