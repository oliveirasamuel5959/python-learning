// Exemplo de boas práticas para nomear ações em um sistema de gerenciamento de estado

app.post('/api/users', (req, res) => {
    // Ação: Criar um novo usuário
    const newUser = req.body;
    // Lógica para adicionar o usuário ao banco de dados
    res.status(201).send({ message: 'Usuário criado com sucesso', user: newUser });
});

app.get('/api/users', (req, res) => {
    // Ação: Obter a lista de usuários
    // Lógica para buscar usuários no banco de dados
    res.status(200).send({ users: [] });
}); 