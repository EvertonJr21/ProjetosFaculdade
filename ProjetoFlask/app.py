from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardapio/<id>')
def pratos(id):
    if int(id) == 1:
        return render_template('hamburguer.html')
    elif int(id) == 2:
        return render_template('lasanha.html')
    elif int(id) == 3:
        return render_template('panqueca.html')
    elif int(id) == 4:
        return render_template('pizza.html')
    else:
        return render_template('erro.html')
            
app.run(debug=True)