from flask import Flask, render_template, request, redirect
from connect import inserir, mostrar_todos, deletar_pessoa, atualizar_pessoa, buscar_CPF
from model import Pessoa

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def cadastrar():
    """Metodo para cadastrar a pessoa"""
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        nome = request.form["nome"]
        cpf = request.form["cpf"]
        dataNascimento = request.form["data"]
        sexo = request.form["sexo"]
        pessoa = Pessoa(cpf, nome, dataNascimento, sexo)
        inserir(pessoa)
        return pessoas_cadastradas()
       
@app.route('/cadastros', methods=['GET'])
def pessoas_cadastradas():
    """Metodo para redirecionar para pagina com todos os cadastros"""
    variavel = mostrar_todos()
    return render_template('pessoas_cadastradas.html', variavel=variavel) 
    
@app.route('/deletar/<string:cpf>')
def deletar(cpf):
    """metodo de deletar pessoa cadastrada"""
    deletar_pessoa(cpf)
    return redirect('/cadastros')

@app.route('/atualizar/<string:cpf>', methods=['GET', 'POST'])
def atualizar(cpf):
    """Metodo para atualizar pessoa ja cadastrada"""
    if request.method == 'GET':
        variavel = buscar_CPF(cpf)
        return render_template('atualizar.html', variavel = variavel)
    elif request.method == 'POST':
        nome = request.form["nome"]
        cpf = request.form["cpf"]
        dataNascimento = request.form["data"]
        sexo = request.form["sexo"]
        pessoa = Pessoa(cpf, nome, dataNascimento, sexo)
        try:
            atualizar_pessoa(cpf, pessoa)
            return redirect('/cadastros')
        except:
            return 'Algo deu errado'
   
if __name__ == '__main__':
    app.run(debug=True)




