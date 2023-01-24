<template><div><h1 id="安装-go-cqhttp" tabindex="-1"><a class="header-anchor" href="#安装-go-cqhttp" aria-hidden="true">#</a> 安装 go-cqhttp</h1>
<div class="custom-container danger"><p class="custom-container-title">为什么需要 go-cqhttp？</p>
<p>青岚 Bot 本身只负责处理 MC与群聊的消息，需要借助 go-cqhttp 与 QQ 进行通信。</p>
<p>同时 青岚 Bot 仅使用 go-cqhttp 进行测试。使用其他 OneBot 实现（如 <a href="https://github.com/yyuueexxiinngg/onebot-kotlin" target="_blank" rel="noopener noreferrer">OneBot Kotlin<ExternalLinkIcon/></a>），请<strong>自行承担</strong>可能存在的<strong>兼容性问题</strong>。</p>
</div>
<div class="custom-container tip"><p class="custom-container-title">提示</p>
<p>脚手架安装的 青岚 Bot 自带 nonebot插件版的go-cqhttp<br>
若选择脚手架安装，则无需安装本页的 go-cqhttp</p>
</div>
<hr>
<div class="custom-container tip"><p class="custom-container-title">准备工作</p>
<ul>
<li>一台服务器或能 24 小时运行的电脑</li>
<li>熟悉电脑基本操作（下载操作文件、安装卸载软件、使用命令行工具如 PowerShell 和 Bash）</li>
</ul>
</div>
<ol>
<li>
<p>下载最新版 <a href="https://github.com/Mrs4s/go-cqhttp/releases/latest" target="_blank" rel="noopener noreferrer">go-cqhttp<ExternalLinkIcon/></a>，不知道下哪个请参考 <a href="https://docs.go-cqhttp.org/guide/quick_start.html#%E4%B8%8B%E8%BD%BD" target="_blank" rel="noopener noreferrer">版本说明<ExternalLinkIcon/></a>。</p>
</li>
<li>
<p>创建一个空文件夹存放数据，并将解压好的 <code v-pre>go-cqhttp</code> 可执行文件放入其中。</p>
</li>
<li>
<p>在当前文件夹内打开一个终端，并运行 <code v-pre>go-cqhttp</code>，选择 <code v-pre>3</code> 反向 Websocket 通信，在文件夹内生成 <code v-pre>config.yml</code> 配置文件。</p>
</li>
<li>
<p>打开 <code v-pre>config.yml</code>，将下方示例内容覆盖或者对照修改原本内容，注意把 <code v-pre>uin</code> 改为自己机器人 QQ 号。</p>
</li>
</ol>
<div class="custom-container warning"><p class="custom-container-title">Windows 用户不要用记事本修改 config.yml</p>
<p>Windows 自带记事本可能导致文本乱码，请使用第三方文本编辑器，如 <a href="https://www.rizonesoft.com/downloads/notepad3/" target="_blank" rel="noopener noreferrer">NotePad3<ExternalLinkIcon/></a>，<a href="https://code.visualstudio.com/Download" target="_blank" rel="noopener noreferrer">VS Code<ExternalLinkIcon/></a>，<a href="http://www.sublimetext.com/3" target="_blank" rel="noopener noreferrer">Sublime Text<ExternalLinkIcon/></a>。</p>
</div>
<p><strong>示例版本：v1.0.0-beta8-fix2</strong></p>
<div class="language-yaml line-numbers-mode" data-ext="yml"><pre v-pre class="language-yaml"><code><span class="token key atrule">account</span><span class="token punctuation">:</span>
  <span class="token key atrule">uin</span><span class="token punctuation">:</span> <span class="token number">1233456</span> <span class="token comment"># 机器人QQ账号</span>

<span class="token key atrule">servers</span><span class="token punctuation">:</span>
  <span class="token punctuation">-</span> <span class="token key atrule">ws-reverse</span><span class="token punctuation">:</span>
      <span class="token key atrule">universal</span><span class="token punctuation">:</span> ws<span class="token punctuation">:</span>//127.0.0.1<span class="token punctuation">:</span>8080/onebot/v11/ws
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><ol start="5">
<li>在终端中重新运行 <code v-pre>go-cqhttp</code>，跟随提示完成扫码登录和安全验证。</li>
</ol>
</div></template>


