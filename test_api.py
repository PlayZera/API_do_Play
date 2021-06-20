from flask import Flask, request
from random import randbytes

a = randbytes(4)
app = Flask("Testando_API")

@app.route("/gerarToken", methods=["GET"])
def gerarToken():
    return{"Token": "{0}".format(a)}

@app.route("/cadastrar_user", methods=["POST"])
def cadastrar_user():

    body = request.get_json()

    print(body)

    return body

app.run()