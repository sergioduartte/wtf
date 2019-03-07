# coding: utf-8
from flask import Flask
from flask import render_template

app = Flask("/wtf") #, template_folder='./templates')

ok = 200
merdao = 404

@app.route("/")
def hello_world():
    return  "deu bom, gerasss o/'"

@app.route("/page/teste/<nome>")
def page(nome):
    return render_template("page.html", nome=nome)

@app.route("/<nome>")
def index(nome):
    if nome.lower() == "teste404":
        return "Not Found", 404
    elif nome.lower() != "":
        return "Iae men, tu ta ligado que tu tá querendo acessar errado né, se liga... kkk<br><br>link quebrado:<br>{}".format(nome), merdao

@app.route("/teste")
@app.route("/teste/<algumaCoisa>")
@app.route("/teste/<algumaCoisa>/<nome>")
def imprime(algumaCoisa=None, nome=None):
    if nome == "sergio":
        return "Oi sejo! <br><strong> \n I'm learning Flask!!</strong>", ok
    if algumaCoisa == "jooj":
        return "iae essa galera! Teste.<br><strong>I'm learning Flask!!</strong>", ok
    return "acho que deu certo", ok

app.run(debug=True, use_reloader=True) #mudar para false antes do deploy