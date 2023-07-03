from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="qinglan-bot",
    version="0.1.5",
    author="17TheWord",
    author_email="17theword@gmail.com",
    description="基于NoneBot的QQ群聊与Minecraft Server消息互通机器人",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/17TheWord/qinglan_bot",
    packages=find_packages(include=['qinglan_bot', 'qinglan_bot.*']),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'mcqq-tool>=0.0.8',
        'nonebot2>=2.0.0',
        'nonebot-adapter-onebot>=2.1.5',
        'nonebot-plugin-guild-patch>=0.2.0',
        'nonebot2[websockets]',
        'websockets>=10.3',
        'tortoise-orm>=0.19.3',
        'aio-mc-rcon>=3.2.0',
        'click>=8.0.4',
    ],
    entry_points={'console_scripts': [
        'ql=qinglan_bot.cli_start:main',
    ]},
)
