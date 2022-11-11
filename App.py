from flask import Flask,request
from rutas.login import login
from flask_cors import CORS

app = Flask(__name__)
#app.register_blueprint(login)
CORS(app)
# @app.route('/login',methods=['POST'])
# def ingreso_login():
#     if request.method == 'POST':
#         usuario = request.form['usuario']
#         password = request.form['password']
#         print(usuario)
#         print(password)
#     return ('INSERTO EXITOSO')
@app.route("/login", methods=['POST'])
def add_user():
    if request.method == 'POST':
        print(request.form['usuario'])
        print(request.form['password'])
        return {"carnet":request.form('ci')}
