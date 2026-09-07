from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS

info = Info(title="Musica Catalogo API", version="1.0.0")

app = OpenAPI(__name__, info=info)

CORS(app)

import Routes.Musica_Rotas

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)