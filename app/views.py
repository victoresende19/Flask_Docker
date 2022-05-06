from flask import render_template
from app import app

@app.route('/')
def home():
    return "<b>There has been a change</b>"

@app.route('/template')
def template():
    return render_template('home.html')

@app.route('/hora')
def hora():
    from datetime import datetime
    return f'Hora: {datetime.now()}'

@app.route('/soma', methods=['GET'])
def soma(a=2, b=3):
    return f'A soma de {a} + {b} é igual a {a+b}'
