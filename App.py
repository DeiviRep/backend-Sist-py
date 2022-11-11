from flask import Flask
from rutas.login import login
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(login)
CORS(app)
