from fastapi import FastAPI
from src.schemas.schemas import Produto

app = FastAPI()

@app.post('/produto')
def criar_produto(produto: Produto):
    return {'Msg': 'Criando'}


@app.get('/produtos')
def listar_produtos():
    return {'Msg': 'Listagem'}