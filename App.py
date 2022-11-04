from flask import Flask, jsonify, request
from usuarios import usuario
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
app.register_blueprint(usuario)

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
    cur.execute('SELECT * FROM login')
    row = cur.fetchall()
    i=0
    login=[]
    for n in row:
        login.append({"id_l":row[i][0],"usuario":row[i][1],"password":row[i][2]})
        i=i+1
    return jsonify(login)

@app.route("/add_user", methods=['POST'])
def add_user():
    if request.method == 'POST':
        print(request.form.get('ci'))
        return {"carnet":request.form.get('ci')}
        
@app.route("/autenticar", methods=['POST'])
def add_user2():
    if request.method == 'POST':
        print(request.form.get('login'))
        usuario = request.form.get('login[1]')
        password = request.form.get('login[2]')
        
        cur = mysql.connection.cursor()
        if cur.execute('SELECT id_l FROM login WHERE usuario = %s and password = %s',(usuario,password)):
            return True
        return False
        
        #mysql.connection.commit()
        