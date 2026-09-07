from pydantic import BaseModel

class MusicaUpdateSchema(BaseModel):
    id: int

    nome: str
    data_criacao: str
    nome_criador: str
    genero: str