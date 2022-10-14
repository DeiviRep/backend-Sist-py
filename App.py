from array import array
from crypt import methods
import json
from urllib import request
from flask import Flask,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
#connectamos
app.config['MYSQL_HOST']='bvcpgguw0kpl5h91bxdy-mysql.services.clever-cloud.com'
app.config['MYSQL_USER']='u4plexpe8n2igv8k'
app.config['MYSQL_PASSWORD']='cgDOAUgJfonIDHUeJeqF'
app.config['MYSQL_DB']='bvcpgguw0kpl5h91bxdy'
mysql = MySQL(app)

app.secret_key= 'mysecretkey'

CORS(app)

@app.route("/")
def holamundo():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM user')
    #cur.execute('SELECT CURDATE();')
    row = cur.fetchall()
    i=0
    usuarios=[]
    for n in row:
        usuarios.append({"nombre":row[i][1],"email":row[i][2],"pasword":row[i][3]})
        i=i+1
    return jsonify(usuarios)

@app.route("/add_user", methods=['POST'])
def add_user():
    if request.method == 'POST':
        print(request.form('ci'))
        return jsonify({"carnet":request.form('ci')})
        