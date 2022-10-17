import os
from flask import request, jsonify
from app import app, mongo


ROOT_PATH = os.environ.get('ROOT_PATH')


@app.route('/usuarios/listarUsuarios', methods = ['GET'])
def listar_usuarios():
    if request.method == 'GET':

        data = mongo.db.usuarios.find({})
        listado_documentos = list(data)

        if data == None:
            data = []
        
        return jsonify({"transaccion":True, "data":listado_documentos})