<template><div><h1 id="安装-mcqq-bot" tabindex="-1"><a class="header-anchor" href="#安装-mcqq-bot" aria-hidden="true">#</a> 安装 MCQQ Bot</h1>
<div class="custom-container warning"><p class="custom-container-title">前提条件</p>
<p>MCQQ Bot 基于 <a href="https://github.com/nonebot/nonebot2" target="_blank" rel="noopener noreferrer">NoneBot2<ExternalLinkIcon/></a> 开发，因此依赖于 <a href="https://www.python.org/downloads/" target="_blank" rel="noopener noreferrer">Python<ExternalLinkIcon/></a>。不会安装 Python 的可以参考 <a href="https://www.liaoxuefeng.com/wiki/1016959663602400/1016959856222624" target="_blank" rel="noopener noreferrer">廖雪峰的教程<ExternalLinkIcon/></a>。</p>
</div>
<div class="custom-container danger"><p class="custom-container-title">警告</p>
<p><a href="https://github.com/nonebot/nonebot2" target="_blank" rel="noopener noreferrer">NoneBot2<ExternalLinkIcon/></a> 与 <a href="https://github.com/nonebot/nonebot" target="_blank" rel="noopener noreferrer">NoneBot<ExternalLinkIcon/></a> <strong>不兼容且无法共存</strong>！如果你曾经使用过 NoneBot 或基于 NoneBot 开发的机器人（如：<a href="https://github.com/pcrbot/yobot" target="_blank" rel="noopener noreferrer">yobot<ExternalLinkIcon/></a>、<a href="https://github.com/Ice-Cirno/HoshinoBot" target="_blank" rel="noopener noreferrer">HoshinoBot<ExternalLinkIcon/></a>、<a href="https://github.com/SK-415/dd-bot" target="_blank" rel="noopener noreferrer">dd-bot<ExternalLinkIcon/></a>），或者你不确定是否安装过 NoneBot。</p>
<p>那么在<strong>开始安装之前</strong>，请先尝试在终端（Powershell/cmd）内执行 <code v-pre>pip uninstall nonebot</code> <strong>卸载</strong> NoneBot，或者创建一个 <a href="https://docs.python.org/zh-cn/3/library/venv.html#creating-virtual-environments" target="_blank" rel="noopener noreferrer">虚拟环境<ExternalLinkIcon/></a> 使 HarukaBot 可以与 NoneBot 共存。</p>
</div>
<h2 id="脚手架安装-推荐" tabindex="-1"><a class="header-anchor" href="#脚手架安装-推荐" aria-hidden="true">#</a> 脚手架安装（推荐）</h2>
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
</ol>
<blockquote>
<p>以后启动只需在<strong>相同文件夹</strong>内执行最后一步即可</p>
</blockquote>
<div class="custom-container tip"><p class="custom-container-title">怎么更新 HarukaBot？</p>
<p>详见 <RouterLink to="/faq.html#%E6%80%8E%E4%B9%88%E6%9B%B4%E6%96%B0-harukabot">常见问题</RouterLink></p>
</div>
<h2 id="从-nonebot2-插件商店安装-适用于-nonebot2-用户" tabindex="-1"><a class="header-anchor" href="#从-nonebot2-插件商店安装-适用于-nonebot2-用户" aria-hidden="true">#</a> 从 NoneBot2 插件商店安装（适用于 NoneBot2 用户）</h2>
<ol>
<li>
<p>使用 <code v-pre>nb-cli</code> 命令从 <a href="https://v2.nonebot.dev/store.html" target="_blank" rel="noopener noreferrer">NoneBot2 商店<ExternalLinkIcon/></a> 安装。</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>nb plugin <span class="token function">install</span> haruka_bot
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
<li>
<p>（可选）在 bot 根目录的 <code v-pre>.env.*</code> 文件中，添加 <code v-pre>HARUKA_DIR=&quot;储存路径&quot;</code> （不设置默认为 <code v-pre>./data/</code>）设置 HarukaBot 数据文件的存储路径。</p>
</li>
<li>
<p>安装完成后重启 <code v-pre>NoneBot2 项目</code> 即可使用。</p>
</li>
</ol>
<h2 id="从-github-安装-包含不稳定的新特性" tabindex="-1"><a class="header-anchor" href="#从-github-安装-包含不稳定的新特性" aria-hidden="true">#</a> 从 GitHub 安装（包含不稳定的新特性）</h2>
<p>安装</p>
<CodeGroup>
<CodeGroupItem title="pip">
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token comment">#master</span>
pip <span class="token function">install</span> <span class="token parameter variable">--upgrade</span> git+https://github.com/SK-415/HarukaBot.git@master
<span class="token comment">#dev</span>
pip <span class="token function">install</span> <span class="token parameter variable">--upgrade</span> git+https://github.com/SK-415/HarukaBot.git@dev
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div></CodeGroupItem>
<CodeGroupItem title="poetry">
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token comment">#master</span>
poetry <span class="token function">add</span> git+https://github.com/SK-415/HarukaBot.git<span class="token comment">#master</span>
<span class="token comment">#dev</span>
poetry <span class="token function">add</span> git+https://github.com/SK-415/HarukaBot.git<span class="token comment">#dev</span>
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div></CodeGroupItem>
</CodeGroup>
<p>运行</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>hb run
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div><h2 id="手动安装-不推荐" tabindex="-1"><a class="header-anchor" href="#手动安装-不推荐" aria-hidden="true">#</a> 手动安装（不推荐）</h2>
<blockquote>
<p>由于历史原因遗留的方法，不再提供支持，非常不推荐使用。</p>
</blockquote>
<ol>
<li>
<p>克隆或下载 HarukaBot 源码到本地。</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code><span class="token function">git</span> clone https://github.com/SK-415/HarukaBot.git
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
<li>
<p>安装依赖。</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>poetry <span class="token function">install</span> --no-dev
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
<li>
<p>启动 HarukaBot</p>
<div class="language-bash line-numbers-mode" data-ext="sh"><pre v-pre class="language-bash"><code>python bot.py
</code></pre><div class="line-numbers" aria-hidden="true"><div class="line-number"></div></div></div></li>
</ol>
</div></template>


