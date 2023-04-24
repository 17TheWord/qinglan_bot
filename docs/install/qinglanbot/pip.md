# 脚手架安装（推荐）

1. 打开终端，并选择一个文件夹用来存放数据。

   ::: tip Windows 用户可以这么做
   打开一个文件夹，对着文件夹内空白处，按住 shift 同时单击鼠标右键 -> 在此处打开 Powershell/命令 窗口。
   :::

2. 在终端内输入以下命令安装脚手架。

   :::: code-group
   ::: code-group-item pip

    ```sh
    pip install qinglan-bot
    ```
   :::
   ::::

   ::: tip 下载慢可以尝试清华源
   <CodeGroup>
   <CodeGroupItem title="pip">

    ```sh
    pip install qinglan-bot -i https://pypi.tuna.tsinghua.edu.cn/simple/
    ```
    </CodeGroupItem>
    </CodeGroup>
    :::

3. 启动 青岚 Bot。
   在空文件夹下输入命令
    ```sh
    ql run
    ```
4. 登录机器人账号
 
   看到这样一条日志后，即可前往 [http://127.0.0.1:8080/go-cqhttp/](http://127.0.0.1:8080/go-cqhttp/) 登录机器人账号了
   ```log
   [INFO] nonebot_plugin_gocqhttp | Startup complete, Web UI has served to http://127.0.0.1:8080/go-cqhttp/
   ```

> 以后启动只需在**相同文件夹**内执行启动命令即可
