from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "Hello,World!"

@app.route('/<usuario>')
def ruta_dinamica(usuario):
	return('<p>Hola,{}.</p>'.format(usuario))
