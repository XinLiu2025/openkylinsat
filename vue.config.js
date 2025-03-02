module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: 'http://152.136.142.183:39010/', // 要代理到的目标服务器
                changeOrigin: true,
                pathRewrite: {
                    '^/api': '', // 可选的路径重写规则
                },
            },
        },
    },
};