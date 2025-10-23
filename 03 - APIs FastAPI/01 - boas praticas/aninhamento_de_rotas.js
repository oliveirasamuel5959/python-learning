app.get('users/{userId}/orders', (req, res) => {
    // Lógica para obter os pedidos de um usuário específico
    res.send(`Lista de pedidos do usuário com ID: ${req.params.userId}`);
})

app.get('users/{userId}/orders/{orderId}', (req, res) => {
    // Lógica para obter um pedido específico de um usuário
    res.send(`Detalhes do pedido com ID: ${req.params.orderId} do usuário com ID: ${req.params.userId}`);
})

app.listen(3000, () => {
    console.log('Servidor rodando na porta 3000');
})