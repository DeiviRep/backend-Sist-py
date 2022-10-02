from array import array
import json
from flask import Flask,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
#connectamos
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='PWEB_PYTHON'
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