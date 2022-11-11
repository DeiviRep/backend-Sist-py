from flask import Flask,request
from rutas.login import login
from flask_cors import CORS

app = Flask(__name__)
#app.register_blueprint(login)
@app.route('/login',methods=['POST'])
def ingreso_login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        print(usuario)
        print(password)
    return ('INSERTO EXITOSO')
CORS(app)
