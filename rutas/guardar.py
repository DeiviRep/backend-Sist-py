from flask import Blueprint
from flask import request
from flask_cors import cross_origin

con()
login = Blueprint('login',__name__)
@login.route('/',methods=['POST'])
@cross_origin(supports_credentials=True)
def ingreso_login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        print(usuario)
        print(password)
    return ('INSERTO EXITOSO')




        # cur = mysql.connection.cursor()
#insert into detalle_login(num_dl,id_login,fecha_finalisar,estado) values('DL10',1,NULL,0);
        # cur.execute("""insert into detalle_login(num_dl,id_login,fecha_finalisar,estado) 
        #                             values('DL10',1,NULL,0);""",(idl,usuario,password,token_cea))
