from sqlalchemy import Column, Integer, String
from Model.Base import Base

class Musica(Base):
    __tablename__ = 'musica'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    data_criacao = Column(String(20))
    nome_criador = Column(String(100))
    genero = Column(String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "data_criacao": self.data_criacao,
            "nome_criador": self.nome_criador,
            "genero": self.genero
        }