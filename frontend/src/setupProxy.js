const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = app => {
    app.use(
        createProxyMiddleware('/endpoint',
            {
                target: 'http://localhost:8000',
                changeOrigin: true,
            })
    )
}