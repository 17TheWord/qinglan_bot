<template><div><h1 id="脚手架安装-推荐" tabindex="-1"><a class="header-anchor" href="#脚手架安装-推荐" aria-hidden="true">#</a> 脚手架安装（推荐）</h1>
<div class="custom-container tip"><p class="custom-container-title">提示</p>
<p>脚手架安装的 MCQQ Bot 自带 nonebot插件版的go-cqhttp<br>
若选择脚手架安装，则无需安装上一节的 go-cqhttp</p>
</div>
<ol>
<li>
<p>打开终端，并选择一个文件夹用来存放数据。</p>
<div class="custom-container tip"><p class="custom-container-title">Windows 用户可以这么做</p>
<p>打开一个文件夹，对着文件夹内空白处，按住 shift 同时单击鼠标右键 -&gt; 在此处打开 Powershell/命令 窗口。</p>
</div>
</li>
<li>
<p>在终端内输入以下命令安装脚手架。</p>
<CodeGroup>
<CodeGroupItem title="pip">
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>pip <span class="token function">install</span> mcqq-bot-test
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></CodeGroupItem>
</CodeGroup>
<div class="custom-container tip"><p class="custom-container-title">下载慢可以尝试清华源</p>
<CodeGroup>
<CodeGroupItem title="pip">
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>pip <span class="token function">install</span> mcqq-bot-test <span class="token parameter variable">-i</span> https://pypi.tuna.tsinghua.edu.cn/simple/
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div> </CodeGroupItem>
 </CodeGroup>
</div>
</li>
<li>
<p>启动 MCQQ Bot。</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>mcqq run
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
<li>
<p>登录机器人账号</p>
<p>看到这样一条日志后，即可前往 <a href="http://127.0.0.1:8080/go-cqhttp/" target="_blank" rel="noopener noreferrer">http://127.0.0.1:8080/go-cqhttp/<ExternalLinkIcon/></a> 登录机器人账号了</p>
<div class="language-log line-numbers-mode" data-ext="log"><pre v-pre class="language-log"><code><span class="token punctuation">[</span><span class="token level info keyword">INFO</span><span class="token punctuation">]</span> nonebot_plugin_gocqhttp <span class="token operator">|</span> Startup complete<span class="token punctuation">,</span> Web UI has served to <span class="token url">http://127.0.0.1:8080/go-cqhttp/</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
</ol>
<blockquote>
<p>以后启动只需在<strong>相同文件夹</strong>内执行最后一步即可</p>
</blockquote>
</div></template>


