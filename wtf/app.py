from flask import Flask

app = Flask("/wtf")

ok = 200
merdao = 404

@app.route("/")
def hello_world():
    return  "o/'", 200
@app.route("/teste")
@app.route("/teste/<algumaCoisa>")
@app.route("/teste/<algumaCoisa>/<nome>")
def imprime(algumaCoisa=None, nome=None):
    if nome == "sergio":
        return "Oi sejo! <br><strong> \n I'm learning Flask!!</strong>", ok
    if algumaCoisa == "jooj":
        return "iae essa galera! Teste.<br><strong>I'm learning Flask!!</strong>", ok
    return "acho que deu certo", ok

# @app.route("/teste/icaro")
# def teste2():
#     return "iae essa galera!<strong> \n oooooh Dessada Sama...</strong>", ok

app.run(debug=True, use_reloader=True) #mudar para false antes do deploy