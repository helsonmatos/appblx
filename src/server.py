from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto

app = FastAPI()

@app.post('/produto')
def criar_produto(produto: Produto, db: Session = Depends(get_db())):
    produto_criado = RepositorioProduto().criar(produto)
    return {'Msg': 'Criando'}


@app.get('/produtos')
def listar_produtos():
    return {'Msg': 'Listagem'}