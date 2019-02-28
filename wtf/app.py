from flask import Flask

app = Flask("/wtf")

ok = 200
merdao = 404

@app.route("/")
def hello_world():
    return "iae essa galera!<strong> \n I'm learning Flask!!</strong>", ok
    

@app.route("/teste")
def teste():
    return "iae essa galera!<strong> \n Querendo...</strong>", ok


@app.route("/teste/icaro")
def teste2():
    return "iae essa galera!<strong> \n oooooh Dessada Sama...</strong>", ok

app.run()