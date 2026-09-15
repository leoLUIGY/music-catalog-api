# Music Catalog API

API responsável pelo **catálogo de músicas**, desenvolvida em **Python / Flask**, como parte de uma arquitetura de microsserviços.

## Tecnologias

* Python 3.9
* Flask
* Flask-OpenAPI3
* Swagger / OpenAPI
* CORS
* Docker

## Executar com Docker

Clone o projeto:

```bash
git clone https://github.com/leoLUIGY/music-catalog-api.git
cd music-catalog-api
```

Crie a imagem:

```bash
docker build -t music-catalog-api .
```

Execute o container:

```bash
docker run -p 5000:5000 music-catalog-api
```

## Swagger

Após iniciar o container, acesse:

```text
http://localhost:5000/openapi/swagger
```

Através do Swagger é possível visualizar e testar as rotas disponíveis da API.

## Objetivo

O serviço é responsável por disponibilizar as operações relacionadas ao **catálogo de músicas**, sendo consumido pelo **Music API Gateway** dentro da arquitetura de microsserviços.
