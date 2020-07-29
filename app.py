from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/selecionar', methods=['GET', 'POST'])
def selecao():
    if request.method == 'POST':
        if request.form['selecao'] == 'js':
            return render_template('juros_simples.html')
        
        if request.form['selecao'] == 'jc':
            return render_template('juros_compostos.html')

@app.route('/simples', methods=['GET', 'POST'])
def valor_simples():
    if request.method == 'POST':
        capital = float(request.form['capital'])
        taxa_juros = float(request.form['taxa_juros'])
        tempo = float(request.form['tempo'])

        juros = capital * (taxa_juros/100) * tempo
        montante = capital + juros

        if request.form['botao'] == 'calcular':
            return render_template('juros_simples.html', juros=f'{juros:.2f}', montante=f'{montante:.2f}')

@app.route('/composto', methods=['GET', 'POST'])
def valor_composto():
    if request.method == 'POST':
        capital = float(request.form['capital'])
        taxa_juros = float(request.form['taxa_juros'])
        tempo = float(request.form['tempo'])

        montante = capital * ((1 + (taxa_juros/100)) ** tempo)
        juros = montante - capital

        if request.form['botao'] == 'calcular':
            return render_template('juros_compostos.html', juros=f'{juros:.2f}', montante=f'{montante:.2f}')
