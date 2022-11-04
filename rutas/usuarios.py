from flask import Blueprint

usuario = Blueprint('usuario',__name__)

@usuario.route('/')
def index():
    return "This is en example app"