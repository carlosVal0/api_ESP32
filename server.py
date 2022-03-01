import json
from flask import Flask, render_template,request,jsonify
from random import choice

words = ["Hola","Saludos","Adios","Control","Angie","Carlos"]


app = Flask(__name__)

@app.route('/',methods=["GET"])
def inicio():
    return jsonify(word = choice(words))


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")