from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/galeria')
def getGaleria():
    obrazki = [
        'https://bit.ly/2Paw95n',
        'https://bit.ly/2Paw95n',
        'https://bit.ly/2Paw95n',
        'https://bit.ly/2Paw95n',
    ]
    return render_template('galeria.html', obrazki=obrazki)



