<template><div><h1 id="进阶设置" tabindex="-1"><a class="header-anchor" href="#进阶设置" aria-hidden="true">#</a> 进阶设置</h1>
<p>这里涉及到了有关 NoneBot 配置文件的相关配置</p>
<p>这些配置并非必须项，如有需求可自行修改</p>
<details class="custom-container details"><summary>示例（点我展开）</summary>
<div class="language-json line-numbers-mode" data-ext="json"><pre v-pre class="language-json"><code>HOST=<span class="token number">0.0</span>.<span class="token number">0.0</span>
PORT=<span class="token number">8080</span>
SUPERUSERS=<span class="token punctuation">[</span><span class="token punctuation">]</span>
NICKNAME=<span class="token punctuation">[</span><span class="token punctuation">]</span>
COMMAND_START=<span class="token punctuation">[</span><span class="token string">""</span><span class="token punctuation">]</span>

MC_QQ_DIR=<span class="token string">"./data/"</span>
MC_QQ_TO_ME=<span class="token boolean">false</span>
MC_QQ_MCRCON_GUILD_ADMIN_ROLES=<span class="token punctuation">[</span><span class="token string">"MCQQ"</span><span class="token punctuation">,</span> <span class="token string">"频道主"</span><span class="token punctuation">]</span>
</code></pre><div class="highlight-lines"><br><br><br><br><br><br><div class="highlight-line">&nbsp;</div><div class="highlight-line">&nbsp;</div><br></div><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div></details>
<h2 id="websocket-地址" tabindex="-1"><a class="header-anchor" href="#websocket-地址" aria-hidden="true">#</a> WebSocket 地址</h2>
<p>默认值：<code v-pre>&quot;127.0.0.1&quot;</code></p>
<ul>
<li>
<p>WebSocket服务器 IP</p>
<div class="language-json line-numbers-mode" data-ext="json"><pre v-pre class="language-json"><code>MC_QQ_IP=<span class="token string">"127.0.0.1"</span>
</code></pre><div class="highlight-lines"><br></div><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
</ul>
<h2 id="websocket-端口" tabindex="-1"><a class="header-anchor" href="#websocket-端口" aria-hidden="true">#</a> WebSocket 端口</h2>
<p>默认值：<code v-pre>8765</code></p>
<ul>
<li>
<p>WebSocket服务器 端口</p>
<div class="language-json line-numbers-mode" data-ext="json"><pre v-pre class="language-json"><code>MC_QQ_WS_PORT=<span class="token number">8765</span>
</code></pre><div class="highlight-lines"><br></div><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
</ul>
<h2 id="数据库路径" tabindex="-1"><a class="header-anchor" href="#数据库路径" aria-hidden="true">#</a> 数据库路径</h2>
<p>默认值：<code v-pre>&quot;./data/&quot;</code></p>
<ul>
<li>
<p>MCQQ Bot 存储数据库的路径，数据库名为 <code v-pre>mcqq.sqlite3</code></p>
<div class="language-json line-numbers-mode" data-ext="json"><pre v-pre class="language-json"><code>MC_QQ_DIR=<span class="token string">"./data/"</span>
</code></pre><div class="highlight-lines"><br></div><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
</ul>
<h2 id="是否启用" tabindex="-1"><a class="header-anchor" href="#是否启用" aria-hidden="true">#</a> 是否启用 <code v-pre>@</code></h2>
<p>默认值：<code v-pre>true</code></p>
<ul>
<li>
<p>在使用命令时，是否需要 <code v-pre>@MCQQ Bot</code></p>
<div class="language-json line-numbers-mode" data-ext="json"><pre v-pre class="language-json"><code>MC_QQ_TO_ME=<span class="token boolean">false</span>
</code></pre><div class="highlight-lines"><br></div><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
</ul>
<h2 id="频道管理员身份组" tabindex="-1"><a class="header-anchor" href="#频道管理员身份组" aria-hidden="true">#</a> 频道管理员身份组</h2>
<p>默认值：<code v-pre>[&quot;频道主&quot;, &quot;管理员&quot;]</code></p>
<ul>
<li>
<p>频道中可以使用发送有效命令的身份组</p>
<ul>
<li>NoneBot 读取配置文件为按行读取，填写后请将他们缩减为一行，如上方示例一样</li>
</ul>
<div class="language-json line-numbers-mode" data-ext="json"><pre v-pre class="language-json"><code>MC_QQ_MCRCON_GUILD_ADMIN_ROLES=<span class="token punctuation">[</span>
  <span class="token string">"管理员"</span><span class="token punctuation">,</span>
  <span class="token string">"服务器OP"</span>
<span class="token punctuation">]</span>
</code></pre><div class="highlight-lines"><br><br><br><br></div><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div></li>
</ul>
</div></template>


