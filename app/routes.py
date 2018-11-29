from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/galery')
def getGalery():
    lista = [
        'https://cdn6.littlethings.com/app/uploads/2017/05/cute-dog-yorkie-600x600.jpg',
        'https://cdn6.littlethings.com/app/uploads/2017/05/cute-dog-yorkie-600x600.jpg',
        'https://cdn6.littlethings.com/app/uploads/2017/05/cute-dog-yorkie-600x600.jpg'
    ]
    return render_template('galeria.html')



