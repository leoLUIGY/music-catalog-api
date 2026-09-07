from app import app
from sqlalchemy.exc import IntegrityError
from flask_openapi3 import Tag
from Schemas.MusicaBuscaSchema import MusicaBuscaSchema
from Schemas.MusicaSchema import MusicaSchema
from Schemas.MusicaUpdateSchema import MusicaUpdateSchema
from Model import *
from flask import redirect

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
musica_tag = Tag(name="Musica", description="Adição, edição, visualização e remoção de uma musica")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.get('/musicas', tags=[musica_tag])
def get_musicas():
    """Buscar musicas do catalogo
    """
    session = Session()
    try:
        musicas = session.query(Musica).all()

        if not musicas:
            return {"Musicas":[]} , 200
        else:
            return [musica.to_dict() for musica in musicas]
    finally:
        session.close()

@app.get('/musica', tags=[musica_tag])
def get_time(query: MusicaBuscaSchema):
    """Buscar uma musica especifica
    """
    musica_id = query.id
    session = Session()
    try:
        musica = session.query(Musica).filter(Musica.id == musica_id).first()
        if not musica:
            error_msg = "Musica não encontrado na base :/"
            return {"mesage": error_msg}, 404
        else:
            return musica.to_dict()
    finally:
        session.close()

@app.post('/musica', tags=[musica_tag])
def add_time(form: MusicaSchema):
    """ Adicionar uma nova musica ao catalogo
    """
    
    musica = Musica(
        nome = form.nome,
        data_criacao = form.data_criacao,
        nome_criador = form.nome_criador,
        genero = form.genero,
       
    )
    session = Session()
    try:
       
        session.add(musica)
        session.commit()
        return musica.to_dict(), 200
    except IntegrityError as e:        
        error_msg = "Musica de mesmo nome já salva na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar nova musica:/"
        return {"mesage": error_msg}, 400
    finally:
        session.close()

@app.put('/musica', tags=[musica_tag])
def update_time(form: MusicaUpdateSchema):
    """Editar informações de uma musica
    """
    musica_id = form.id
    session = Session()
    try:
        musica = session.query(Musica).filter(Musica.id == musica_id).first()
        if not musica:
            error_msg = "Musica não encontrada na base :/"
            return {"mesage": error_msg}, 404
        else:
            
            musica.nome = form.nome
            musica.data_criacao = form.data_criacao
            musica.nome_criador = form.nome_criador
            musica.genero = form.genero

        
            session.commit()
            return musica.to_dict(), 200
    except IntegrityError as e:        
        error_msg = "musica de mesmo nome já salva na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar nova musica:/"
        return {"mesage": error_msg}, 400
    finally:
        session.close()

@app.delete('/musica', tags=[musica_tag])
def delete_time(query: MusicaBuscaSchema):
    """Deletar um musica a partir do id informado
    """
    musica_id = query.id
    session = Session()
    try:
        count = session.query(Musica).filter(Musica.id == musica_id).delete()
        session.commit()

        if count:
            return {"mesage": "musica removida", "id": musica_id}
        else:
            error_msg = "musica não encontrada na base :/"
            return {"mesage": error_msg}, 404
    finally:
        session.close()