from flask import Flask
from flask_restful import Api
from models.empresas import empresas
from models.usuario_api_valida import usuarios

app = Flask(__name__)
api = Api(app)


api.add_resource(empresas, '/empresas/find/<string:nome>')
# api.add_resource(empresas, '/empresas/update/<int:id>')
# api.add_resource(usuarios, '/usuarios/get/<string:search>')
api.add_resource(usuarios, '/usuarios/edit/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)