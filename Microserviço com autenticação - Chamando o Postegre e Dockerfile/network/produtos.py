import flask

from controller.produtos_controller import ControllerProdutos
from werkzeug.security import check_password_hash
from flask_httpauth import HTTPTokenAuth

produtos = flask.Blueprint("produtos", __name__)

auth = HTTPTokenAuth(scheme='Bearer')

tokens = {
    "admin": 1234
}

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]
    
@produtos.route("/cadastro", methods=["POST"])
@auth.login_required
def cadastro():
    controller = ControllerProdutos()
    request = flask.request.get_json()
    id = controller.cadastrar_produto(request["nome"], request["preco"])
    return flask.jsonify({"status": "OK", "message": "Produto cadastrado com sucesso", "id": id})


@produtos.route("/consulta", methods=["GET"])
@auth.login_required
def consulta():
    controller = ControllerProdutos()
    produtos = controller.get_produtos()
    return flask.jsonify({"produtos": produtos})

@produtos.route("/consulta/<id>", methods=["GET"])
@auth.login_required
def consulta_por_id(id):
    controller = ControllerProdutos()
    produtos = controller.get_produto_por_id(id)
    return flask.jsonify({"produtos": produtos})