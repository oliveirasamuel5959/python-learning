app.get('/products', (req, res) => {
    // Lógica para obter a lista de usuários
    res.send('Lista de usuários');
})

app.get('/products/{id}', (req, res) => {
    // Retorna um produto específico pelo ID
    res.send(`Detalhes do produto com ID: ${req.params.id}`);
})

app.post('/products', (req, res) => {
    // Lógica para criar um novo produto
    res.send('Produto criado com sucesso');
})

app.put('/products/{id}', (req, res) => {
    // Lógica para atualizar um produto existente pelo ID
    res.send(`Produto com ID: ${req.params.id} atualizado com sucesso`);
})

app.delete('/products/{id}', (req, res) => {
    // Lógica para deletar um produto pelo ID
    res.send(`Produto com ID: ${req.params.id} deletado com sucesso`);
})

// Exemplo de requisição GET para obter a lista de produtos
fetch('/products', {method: 'GET'})
.then(response => response.json())
.then(data => console.log(data));

// Exemplo de requisição POST para criar um novo produto
fetch('/products', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({name: 'Novo Produto', price: 100})
})
.then(response => response.json())
.then(data => console.log(data));

