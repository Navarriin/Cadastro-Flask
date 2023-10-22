from model import Pessoa
from flask import Flask, render_template, request, redirect
from connect import inserir, mostrar_todos, mostrar_tab, deletar_pessoa, atualizar_pessoa
import pandas as pd


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':

        nome = request.form["nome"]
        cpf = request.form["cpf"]
        dataNascimento = request.form["data"]
        pessoa = Pessoa(cpf, nome, dataNascimento)
        inserir(pessoa)
        return pessoas_cadastradas()
       
@app.route('/cadastros', methods=['GET'])
def pessoas_cadastradas():
    variavel = mostrar_todos()
    return render_template('pessoas_cadastradas.html', variavel=variavel) 
    

if __name__ == '__main__':
    app.run(debug=True)




