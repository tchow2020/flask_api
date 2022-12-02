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
        sql = "select * from user where nome like '%"+str(search)+"%' or email like '%"+str(search)+"%'"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return jsonify(rows)

 