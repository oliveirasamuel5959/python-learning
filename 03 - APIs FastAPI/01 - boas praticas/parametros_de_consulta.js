// Parametros de consulta em Node.js com Express
const baseUrl = 'https://api.exemplo.com/items';
const params = new URLSearchParams({
    category: 'books',
    page: 1,
    limit: 10,
    sort: 'price'
});

fetch(`${baseUrl}?${params.toString()}`)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Erro:', error));


// Em FastAPI, o equivalente seria:
/*
from fastapi import FastAPI, Query
app = FastAPI()

@app.get("/items/")
def read_items(page: int = Query(1, description="Número da página"), limit: int = Query(10, description="Número de itens por página")):
    return {"page": page, "limit": limit}
*/  
// Neste exemplo, criamos um endpoint '/items' que aceita parametros de consulta 'page' e 'limit' com valores padrão.
