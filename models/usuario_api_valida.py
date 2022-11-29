from flask_restful import Resource
from flask import jsonify, request
from config import banco


class usuarios(Resource):
    conn = None 

    def __init__(self):
        self.conn = banco

    def post(self):
        cursor = self.conn.cursor()
        sql =  "insert into user (nome, email, id) values(%s,%s,%s)"
        cursor.execute(sql, ('', '', 4))
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return {'mensage': 'dados inseridos'}

    def get(self, search):
        cursor =  self.conn.cursor()
        sql = "select * from user where nome like '%"+{search}+"%' or email like '%"+{search}+"%'"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return jsonify(rows)

    def put(self, user_id, empresa_id):
        cursor =  self.conn.cursor()
        sql = "update usuario_empresa set '%"+{empresa_id}+"%' = 2 where '%"+{user_id}+"%' = 1"
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return {'mensage': 'dados atualizados'}