import {defaultTheme} from 'vuepress'
import {searchPlugin} from '@vuepress/plugin-search'

module.exports = {
    title: '青岚',
    description: '青岚Bot',
    base: '/qinglan_bot/',
    locales: {
        '/': {
            lang: 'zh-CN',
        }
    },
    head: [['link', {rel: 'icon', href: '/favicon.jpg'}]],
    plugins: [
        searchPlugin({}),
    ],
    theme: defaultTheme({
        notFound: ["404 Not Found，页面丢失。"],
        backToHome: "<-回到首页",
        repo: '17TheWord/qinglan_bot',
        navbar: [
            {
                text: '首页',
                link: '/',
            },
            {
                text: '安装',
                link: '/install/',
            },
            {
                text: '功能列表',
                link: '/usage/',
            },
            {
                text: '关于',
                link: '/about.md',
            },
        ],

        //左侧列表
        sidebar: {
            '/install/': [
                '/install/README.md',
                '/install/go-cqhttp',
                {
                    text: '安装 青岚 Bot',
                    children: [
                        '/install/qinglanbot/README.md',
                        '/install/qinglanbot/pip',
                        '/install/qinglanbot/nonebot',
                    ]
                },
                '/install/congrats',
            ],
            '/usage/': [
                '/usage/README.md',
                '/usage/settings.md',
            ],
        },
    }),
}
