// Exemplo de versionamento de rotas em uma API RESTful usando Express.js
const express = require('express');
const app = express();
const port = 3000;

// Versão 1 da API
app.get('/api/v1/products', (req, res) => {
    // Lógica para retornar a lista de produtos da versão 1
    res.status(200).send({ version: 'v1', products: [] });
});

// Versão 2 da API
app.get('/api/v2/products', (req, res) => {
    // Lógica para retornar a lista de produtos da versão 2
    res.status(200).send({ version: 'v2', products: [], nome: 'Novo campo na v2' });
});

app.listen(port, () => {
    console.log(`API rodando em http://localhost:${port}`);
});