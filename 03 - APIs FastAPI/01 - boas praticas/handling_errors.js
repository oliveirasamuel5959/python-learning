/* Códigos de status HTTP em Node.js com Express

código 1XX - Informativo
Exemplo: 100 Continue
Indica que a solicitação inicial foi recebida e o cliente pode continuar com a solicitação.

código 2XX - Sucesso
Exemplo: 200 OK
Exemplo: 201 Created
Exemplo: 204 No Content
Indica que a solicitação foi bem-sucedida e o servidor retornou os dados solicitados.

código 3XX - Redirecionamento
Exemplo: 301 Moved Permanently
Indica que o recurso solicitado foi movido permanentemente para uma nova URL.

código 4XX - Erro do Cliente
Exemplo: 400 Bad Request
Exemplo: 401 Unauthorized
Exemplo: 403 Forbidden
Ex
Exemplo: 404 Not Found
Indica que o recurso solicitado não foi encontrado no servidor.

código 5XX - Erro do Servidor
Exemplo: 500 Internal Server Error
Indica que ocorreu um erro interno no servidor ao processar a solicitação.
Em FastAPI, o equivalente seria:
from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.get("/resource")
def read_resource():
    resource = None  # Simulando recurso não encontrado
    if not resource:
        raise HTTPException(status_code=404, detail="Recurso não encontrado")
    return resource

*/

const express = require('express');
const app = express();

app.get('/resource', (req, res) => {
    const resource = null; // Simulando recurso não encontrado
    if (!resource) {
        return res.status(404).json({ error: 'Recurso não encontrado' });
    }
    res.status(200).json(resource);
});

app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Erro interno do servidor' });
});

app.listen(3000, () => {
    console.log('Servidor rodando na porta 3000');
}); 
