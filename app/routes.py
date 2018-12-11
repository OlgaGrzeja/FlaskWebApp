from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/galeria')
def galeria():
    #Tak sie nie robi ale jakos trza zaczac
    obrazki = [
        'http://www.koty.pl/wp-content/uploads/2017/11/shutterstock_589722092-e1510059950350.jpg',
        'http://www.koty.pl/wp-content/uploads/2017/11/shutterstock_589722092-e1510059950350.jpg',
        'http://www.koty.pl/wp-content/uploads/2017/11/shutterstock_589722092-e1510059950350.jpg',
        'http://www.koty.pl/wp-content/uploads/2017/11/shutterstock_589722092-e1510059950350.jpg',
    ]
   
    return render_template('galeria.html', obrazki=obrazki)

@app.route('/alexa')
def alexa():
    return render_template('alexa.html')


