import psycopg2

class ProdutosDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="postgres",
            database="postgres"
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS produtos (id SERIAL PRIMARY KEY, nome VARCHAR(255), preco DECIMAL(10,2))")

    def get_produtos(self):
        self.cursor.execute("SELECT * FROM produtos")
        rows = self.cursor.fetchall()
        print(rows)
        return rows

    def cadastrar_produto(self, nome, preco):
        sql = "INSERT INTO produtos (nome, preco) VALUES (%s, %s) RETURNING id"
        val = (nome, preco)
        self.cursor.execute(sql, val)
        id = self.cursor.fetchone()[0]
        self.conn.commit()
        return id
    
    def get_produto_por_id(self, id):
        sql = "SELECT * FROM produtos WHERE id = %s"
        val = (id,)
        self.cursor.execute(sql, val)
        row = self.cursor.fetchone()
        return row
