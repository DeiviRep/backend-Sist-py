from flask import Flask
from rutas.login import login
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app,supports_credentials=True)
app.register_blueprint(login)
