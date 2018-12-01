from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html', title="Home Page")

@app.route('/galeria')
def getGalery():
    listaObrazkow = [
        'https://bit.ly/2zuMWLJ',
        'https://bit.ly/2zuMWLJ',
        'https://bit.ly/2zuMWLJ',
        'https://bit.ly/2zuMWLJ',
        'https://bit.ly/2zuMWLJ'
    ]
    return render_template('galeria.html', listaObrazkow=listaObrazkow, title="Galeria")


