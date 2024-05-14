from flask import Flask

from network.produtos import produtos

app = Flask(__name__)

app.register_blueprint(produtos, url_prefix="/api")

app.run()