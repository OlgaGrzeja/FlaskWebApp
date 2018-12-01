from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html', title="Home Page", )

@app.route('/galeria')
def getGalery():
    return render_template('galeria.html')

@app.errorhandler(404)
def error404(error):
    return '<h1>Error cie doszedl</h1>'
