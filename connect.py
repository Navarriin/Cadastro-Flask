from tinydb import TinyDB, Query
from model import Pessoa
import pandas as pd

bd = TinyDB('Pessoas.json')
usuario = Query()

def inserir(model: Pessoa):
    """insere pessoa no banco de dados"""
    bd.insert(
       { 'CPF': model.CPF,
        'Nome': model.nome,
        'DataNascimento': model.dataNascimento,
        'Sexo': model.sexo
        }
    )
    
def mostrar_todos():
    """mostra todos cadastros no banco de dados"""
    todos = bd.all()
    return todos

def mostrar_tab():
    """mostrando todos os cadastros mas em uma tabela"""
    todos = pd.DataFrame(bd)
    return todos

def deletar_pessoa(cpf: str):
    """deleta um usuario no banco de dados"""
    if bd.search(usuario.CPF == str(cpf)):
        bd.remove(usuario.CPF == str(cpf))
    else:
        print('Usuario nao encontrado')

def atualizar_pessoa(cpf: str, model: Pessoa):
    """atualiza um usuario no banco de dados"""
    if bd.search(usuario.CPF == str(cpf)):
        bd.remove(usuario.CPF == str(cpf))
        inserir(model)
        
    else:
        print('Usuario nao encontrado')

def buscar_CPF(cpf):
    """busca a pessoa pelo cpf"""
    return bd.search(usuario.CPF == str(cpf))

