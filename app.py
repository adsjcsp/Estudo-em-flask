

from flask import Flask, Flask, render_template, request, url_for, flash, redirect
app = Flask(__name__)

app.config['SECRET_KEY'] = ''


@app.route("/")
def home():
    nome = request.args.get('nome', 'Alex Douglas')

    return render_template('index.html', nome=nome)


@app.route("/login" methods=('GET', 'POST'))
def initlogin():
    return render_template('login.html')

### -------------------------------------------------------------------------------
#                               Blog
@app.route("/criarpost")
def criarpost():
    return render_template('criar_poost.html')

### -------------------------------------------------------------------------------


@app.route("/login/<nome_usuario>")
def login(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)

@app.route("/sobre")
def sobre():
    
    return render_template('sobre.html')
@app.route("/contato")

def contato():

    return render_template('contato.html')

if __name__== '__main__':
    app.run()
