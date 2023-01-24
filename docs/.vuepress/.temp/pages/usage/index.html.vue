<template><div><h1 id="功能列表" tabindex="-1"><a class="header-anchor" href="#功能列表" aria-hidden="true">#</a> 功能列表</h1>
<div class="custom-container warning"><p class="custom-container-title">注意</p>
<p>群里使用命令前<strong>需要</strong> @机器人，如 <code v-pre>@青岚Bot ql帮助</code>。</p>
<p>如果<strong>不希望</strong>在使用命令前 @机器人，请查看 <a href="./settings">进阶配置</a>。</p>
</div>
<hr>
<h2 id="帮助" tabindex="-1"><a class="header-anchor" href="#帮助" aria-hidden="true">#</a> 帮助</h2>
<ul>
<li>命令：<code v-pre>ql帮助</code></li>
<li>获取目前 青岚 Bot 支持的所有功能指令。</li>
</ul>
<div class="custom-container tip"><p class="custom-container-title">提示</p>
<p>功能表会随版本变化，请以自己机器人帮助信息为准。</p>
</div>
<h2 id="互通列表" tabindex="-1"><a class="header-anchor" href="#互通列表" aria-hidden="true">#</a> 互通列表</h2>
<ul>
<li>命令：<code v-pre>互通列表</code></li>
<li>场景：<code v-pre>群聊丨管理员</code></li>
<li>描述：获取当前 <code v-pre>群聊丨子频道</code> 所互通的服务器列表。</li>
</ul>
<h2 id="已连接服务器列表" tabindex="-1"><a class="header-anchor" href="#已连接服务器列表" aria-hidden="true">#</a> 已连接服务器列表</h2>
<ul>
<li>命令：<code v-pre>已连接服务器列表</code></li>
<li>场景：<code v-pre>管理员</code></li>
<li>描述：获取已经连接至 <code v-pre>WebSocket</code> 的所有服务器。</li>
</ul>
<h2 id="服务器列表" tabindex="-1"><a class="header-anchor" href="#服务器列表" aria-hidden="true">#</a> 服务器列表</h2>
<ul>
<li>命令：<code v-pre>服务器列表</code></li>
<li>场景：<code v-pre>管理员</code></li>
<li>描述：获取数据库中已经记录的服务器列表。</li>
</ul>
<h2 id="互通" tabindex="-1"><a class="header-anchor" href="#互通" aria-hidden="true">#</a> 互通</h2>
<ul>
<li>命令：<code v-pre>开启互通 ServerName</code>丨<code v-pre>关闭互通 ServerName</code></li>
<li>场景：<code v-pre>群聊丨管理员</code></li>
<li>描述：当前群聊与名为 <code v-pre>ServerName</code> 的服务器互通。</li>
</ul>
<h2 id="是否发送群名" tabindex="-1"><a class="header-anchor" href="#是否发送群名" aria-hidden="true">#</a> 是否发送群名</h2>
<ul>
<li>命令：<code v-pre>开启发送群名</code>丨<code v-pre>关闭发送群名</code></li>
<li>场景：<code v-pre>群聊丨管理员</code></li>
<li>描述：当前群聊名称随着群员消息一并发送至MC，并显示在群员昵称之前。</li>
</ul>
<h2 id="是否发送服务器名" tabindex="-1"><a class="header-anchor" href="#是否发送服务器名" aria-hidden="true">#</a> 是否发送服务器名</h2>
<ul>
<li>命令：<code v-pre>开启服务器名 ServerName</code>丨<code v-pre>关闭服务器名 ServerName</code></li>
<li>场景：<code v-pre>管理员</code></li>
<li>描述：名为 <code v-pre>ServerName</code> 的服务器发送至群的消息中，添加服务器名称前缀 <code v-pre>[ServerName]</code>。</li>
</ul>
<h2 id="rcon消息" tabindex="-1"><a class="header-anchor" href="#rcon消息" aria-hidden="true">#</a> Rcon消息</h2>
<ul>
<li>命令：<code v-pre>开启rcon消息 ServerName</code>丨<code v-pre>关闭rcon消息 ServerName</code></li>
<li>场景：<code v-pre>管理员</code></li>
<li>描述：发送至 <code v-pre>ServerName</code> 的消息采用 <code v-pre>Rcon</code> 发送，适用于支持Rcon的<strong>非插件服务端</strong>。</li>
</ul>
<h2 id="rcon命令" tabindex="-1"><a class="header-anchor" href="#rcon命令" aria-hidden="true">#</a> Rcon命令</h2>
<ul>
<li>命令：<code v-pre>开启rcon命令 ServerName</code>丨<code v-pre>关闭rcon命令 ServerName</code></li>
<li>场景：<code v-pre>管理员</code></li>
<li>描述：发送至 <code v-pre>ServerName</code> 的命令采用 <code v-pre>Rcon</code> 发送，适用于所有支持Rcon的服务端。</li>
<li>使用：
<ul>
<li>开启后，发送 <code v-pre>/mcc give player1 apple 1</code> 将会给予玩家 <code v-pre>player1</code> 一个苹果</li>
<li>其中 <code v-pre>/</code> 为nb配置中的命令头</li>
</ul>
</li>
</ul>
<h2 id="修改-rcon-ip" tabindex="-1"><a class="header-anchor" href="#修改-rcon-ip" aria-hidden="true">#</a> 修改 Rcon IP</h2>
<ul>
<li>命令：<code v-pre>修改rconip ServerName ip</code></li>
<li>场景：<code v-pre>私聊丨超级用户</code></li>
<li>描述：修改名为 <code v-pre>ServerName</code> 服务器的 Rcon IP。</li>
<li>使用：
<ul>
<li>发送 <code v-pre>修改rconip server1 localhost</code> 会将名为 <code v-pre>server1</code> 服务器的 <code v-pre>Rcon_IP</code> 改为 <code v-pre>localhost</code></li>
</ul>
</li>
<li>注意：
<ul>
<li>所有开启互通的服务器默认 RconIP 均为 <code v-pre>127.0.0.1</code></li>
<li>若有远程服务器，请自行修改</li>
</ul>
</li>
</ul>
<h2 id="修改-rcon-端口" tabindex="-1"><a class="header-anchor" href="#修改-rcon-端口" aria-hidden="true">#</a> 修改 Rcon 端口</h2>
<ul>
<li>命令：<code v-pre>修改rcon端口 ServerName port</code></li>
<li>场景：<code v-pre>私聊丨超级用户</code></li>
<li>描述：修改名为 <code v-pre>ServerName</code> 服务器的 Rcon 端口。</li>
<li>使用：
<ul>
<li>发送 <code v-pre>修改rcon端口 server1 25576</code> 会将名为 <code v-pre>server1</code> 服务器的 <code v-pre>Rcon_Port</code> 改为 <code v-pre>25576</code></li>
</ul>
</li>
<li>注意：
<ul>
<li>所有开启互通的服务器默认 Rcon端口 均为 <code v-pre>25575</code></li>
<li>若有多个服务器使用Rcon连接，请务必修改成不同的端口</li>
</ul>
</li>
</ul>
<h2 id="修改-rcon-密码" tabindex="-1"><a class="header-anchor" href="#修改-rcon-密码" aria-hidden="true">#</a> 修改 Rcon 密码</h2>
<ul>
<li>命令：<code v-pre>修改rcon密码 ServerName password</code></li>
<li>场景：<code v-pre>私聊丨超级用户</code></li>
<li>描述：修改名为 <code v-pre>ServerName</code> 服务器的 Rcon 密码。</li>
<li>使用：发送 <code v-pre>修改rcon密码 server1 123456789</code> 会将名为 <code v-pre>server1</code> 服务器的 <code v-pre>Rcon_PassWord</code> 改为 <code v-pre>123456789</code></li>
<li>注意：
<ul>
<li>所有开启互通的服务器默认 Rcon密码 均为 <code v-pre>change_password</code></li>
<li>若要使用 Rcon 请务必在使用前修改密码，并确保与服务器端一致，否则不会进行连接</li>
</ul>
</li>
</ul>
</div></template>


