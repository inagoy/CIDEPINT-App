export const devServer = {
    proxy: {
        '/api': {
            target: 'http://localhost:5000',
            changeOrigin: true,
            pathRewrite: {
                '^/api': '',
            },
        },
    },
};