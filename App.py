import json
from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def holamundo():
    return jsonify({"nombre":"Miguel"})