from flask_restful import Resource
from flask import jsonify, request
from config import banco


class usuario_empresa(Resource):
    onn = None 

    def __init__(self):
        self.conn = banco

    def put(self):
        cursor =  self.conn.cursor()
        usuario_id = str(request.json['user_id'])
        empresa_id = str(request.json['empresa_id'])
        sql = f"update usuario_empresa set empresa_id = {empresa_id} where usuario_id = {usuario_id}"
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return {'mensage': 'dados atualizados'}    