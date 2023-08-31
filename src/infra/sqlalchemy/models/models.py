from sqlalchemy import Column, Integer


class Produto():

    __tablename__ = 'Produto'

    id = Column(Integer, primary_key= True, index=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(String)
    disponivel = Column(Boolean)
