// server.js
const serverless = require('serverless-http');
const express = require('express');
const path = require('path');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

// Serve static files
app.use(express.static(path.join(__dirname, '../../staticfiles')));

// Proxy to Django
const proxy = createProxyMiddleware({
  target: 'http://localhost:8000',
  changeOrigin: true,
  ws: true,
});

app.use('/', proxy);

// Handle 404s
app.use((req, res) => {
  res.status(404).sendFile(path.join(__dirname, '../../staticfiles/404.html'));
});

module.exports.handler = serverless(app);
