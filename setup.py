import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="qinglan-bot",  # 项目名称，保证它的唯一性，不要跟已存在的包名冲突即可
    version="0.1.1",  # 程序版本
    author="17TheWord",  # 项目作者
    author_email="17theword@gmail.com",  # 作者邮件
    description="基于NoneBot的QQ群聊与Minecraft Server消息互通机器人",  # 项目的一句话描述
    long_description=long_description,  # 加长版描述？
    long_description_content_type="text/markdown",  # 描述使用Markdown
    url="https://github.com/17TheWord/qinglan_bot",  # 项目地址
    packages=["qinglan_bot"],
    classifiers=[
        "Programming Language :: Python :: 3.9",  # 使用Python3.9
        "License :: OSI Approved :: GNU Affero General Public License v3",  # 开源协议
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'mcqq-tool==0.0.4',
        'nonebot2>=2.0.0',
        'nonebot-adapter-onebot>=2.1.5',
        'nonebot-plugin-guild-patch>=0.2.0',
        'nonebot-plugin-gocqhttp>=0.6.3',
        'websockets>=10.3',
        'tortoise-orm>=0.19.3',
        'aio-mc-rcon>=3.2.0',
        'click>=8.0.4',
    ],
    entry_points={'console_scripts': [
        'ql=qinglan_bot.cli_start:main',
    ]},
)
