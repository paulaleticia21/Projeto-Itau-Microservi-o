import requests
import os
from flask import Flask, jsonify, request, redirect
from flask_mysqldb import MySQL
from flask_restful import Api, Resource
from mysql.connector import connect

app = Flask(__name__)
api = Api(app)
port = int(os.environ.get('PORT', 5000))

@app.route("/")

def home():
    return "Olá Paulinha - seu microserviço"
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)
    
# Configurações do Banco de Dados MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'produtos'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Inicializando o mysql
mysql = MySQL(app)

# Fazendo a implementação do microserviço de produtos no banco de dados Mysql
class ProdutoResource(Resource):
    def get(self, id=None):
        if id is None:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM tb_produtos")
            produtos = cur.fetchall()
            cur.close()
            return jsonify(produtos)
        else:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM tb_produtos WHERE id = %s", (id,))
            produto = cur.fetchone()
            cur.close()
            if produto:
                return jsonify(produto)
            else:
                return {'mensagem': 'Produto não encontrado'}, 404
   
# Configuração da API Gateway
class APIGateway(Resource):
    def get(self):
        return redirect('/api/produtos')

api.add_resource(APIGateway, '/')
api.add_resource(ProdutoResource, '/api/produtos', '/api/produtos/<int:id>')

# Executa o aplicativo Flask
if __name__ == '__main__':
    app.run()

    
    


