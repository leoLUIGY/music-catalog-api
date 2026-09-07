from pydantic import BaseModel

class MusicaSchema(BaseModel):
    nome: str
    data_criacao: str
    nome_criador: str
    genero: str