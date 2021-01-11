from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home/<int:id>') # 127.0.0.1:5000/home/int
def home(id):
    i = id ** 2
    return render_template('index.html', resultado=i)


@app.route('/home/<string:nome>') # 127.0.0.1:5000/home/nome
def home2(nome):
    return f'<h3>{nome}</h3>'


@app.route('/') # 127.0.0.1:5000
def index():
    return '<h1 style="color: blue">index <button>clique aqui</button>'


if __name__ == "__main__":
    app.run(debug=True)
