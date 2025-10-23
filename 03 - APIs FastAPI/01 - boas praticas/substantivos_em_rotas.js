// Rota correta utilizando substantivo no plural
app.get('/users', (req, res) => {
    // Lógica para obter a lista de usuários
    res.send('Lista de usuários');
})

// Rota incorreta utilizando verbo
app.get('/getUsers', (req, res) => {
    // Lógica para obter a lista de usuários
    res.send('Lista de usuários');
})