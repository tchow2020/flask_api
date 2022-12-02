from flask import Flask
from flask_restful import Api
from models.empresas import empresas
from models.usuarios import usuarios
from models.usuario_empresa_api import usuario_empresa

app = Flask(__name__)
api = Api(app)


# api.add_resource(empresas, '/empresas/find/<string:nome>')
api.add_resource(empresas, '/empresas/update/<int:id>')
api.add_resource(usuarios, '/usuarios/get/<string:search>')
api.add_resource(usuario_empresa, '/usuario_empresa/edit')


if __name__ == '__main__':
    app.run(debug=True)