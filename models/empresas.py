from flask_restful import Resource
from flask import jsonify, request
from config import banco


class empresas(Resource):
    conn = None

    def __init__(self):
        self.conn = banco

    def post(self, nome):
        cursor = self.conn.cursor()
        sql =  "insert into verttice (id, nome, status) values(%s,%s,%s)"
        cursor.execute(sql, (2, 'Verttice', 'A'))
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return {'mensage': 'dados inseridos'}

    def get(self, nome):
        cursor = self.conn.cursor()
        sql = "select * from verttice where nome like '%"+str(nome)+"%'" 
        cursor.execute(sql)
        rows = cursor.fetchall()
        return jsonify(rows)

    def put(self, nome):
        cursor = self.conn.cursor()
        sql = """update verttice set status = 'I' where id = '1'"""
        cursor.execute(sql, nome)
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return {'mensage': 'dados atualizados'}
