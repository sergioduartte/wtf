# coding: utf-8
from flask import Flask
from flask import render_template
#from flask import jsonify

app = Flask("/wtf") #, template_folder='./templates')

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
        return "Iae men, tu ta ligado que tu tá querendo acessar errado né, se liga... kkk<br><br>link quebrado:<br>{}".format(nome), 404

@app.route("/teste")
@app.route("/teste/<algumaCoisa>")
@app.route("/teste/<algumaCoisa>/<nome>")
def imprime(algumaCoisa=None, nome=None):
    if nome == "sergio":
        return "Oi sejo! <br><strong> \n I'm learning Flask!!</strong>", 200
    if algumaCoisa == "jooj":
        return "iae essa galera! Teste.<br><strong>I'm learning Flask!!</strong>", 200
    return "acho que deu certo", 200
'''
def json_api():
    pessoas = [{"nome": "Sérgio Duarte"},
                {"nome": "Icaro Jooj"},
                {"nome": "Joasley BrobroBoy"},
                {"nome": "Joaber Cloud Boe"},
                {"nome": "Kaio Supernerd"}]
    return jsonify(pessoas=pessoas, total=len(pessoas))
'''
    

app.run(debug=True, use_reloader=True) #mudar para false antes do deploy