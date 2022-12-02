from flask_restful import Resource
from flask import jsonify, request
from config import banco


class empresas(Resource):
    conn = None

    def __init__(self):
        self.conn = banco

    def post(self, nome):
        cursor = self.conn.cursor()
        sql =  "insert into empresas (id, nome, status) values(%s,%s,%s)"
        cursor.execute(sql, (2, 'empresas', 'A'))
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return {'mensage': 'dados inseridos'}

    def get(self, nome):
        cursor = self.conn.cursor()
        sql = "select * from empresas where nome like '%"+str(nome)+"%'" 
        cursor.execute(sql)
        rows = cursor.fetchall()
        return jsonify(rows)

    def put(self, id):
        cursor = self.conn.cursor()
        resultado = self.verificationAction(request.json['action'])
        sql = "update empresas set status = '"+resultado+"' where id = "+str(id)
        cursor.execute(sql)
        self.conn.commit()
        return {'mensage': 'dados atualizados'}

    def verificationAction(self, action=0):
        if action == 'activate':
            return 'A'
        elif action == 'disable':
            return 'I'
        elif action == 'disableall':
            return 'X'
        return 'A'