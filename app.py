from flask import Flask
from flask_restful import Api
# from config import banco
from models.empresas import empresas


app = Flask(__name__)
api = Api(app)


api.add_resource(empresas, '/empresas/find/<string:nome>')

if __name__ == '__main__':
    app.run(debug=True)