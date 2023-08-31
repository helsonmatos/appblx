from sqlalchemy.orm import Session
from src.schema import schemas

class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db

    def criar(self):
        pass

    def listar(self):
        pass

    def obter(self):
        pass

    def remover(self):
        pass