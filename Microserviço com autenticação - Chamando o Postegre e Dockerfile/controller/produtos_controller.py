from models.produtos_db import ProdutosDB

class ControllerProdutos():
    
    def __init__(self):
        self.database = ProdutosDB()
    
    def get_produtos(self):
        return self.database.get_produtos()
    
    def get_produto_por_id(self,id):
        return self.database.get_produto_por_id(id)
    
    def cadastrar_produto(self, nome, preco):
        return self.database.cadastrar_produto(nome, preco)