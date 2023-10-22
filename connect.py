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
        'DataNascimento': model.dataNascimento
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
    if bd.search(usuario.CPF == cpf):
        bd.remove(usuario.CPF==cpf)
    else:
        print('Usuario nao encontrado')

def atualizar_pessoa(cpf: str, model: Pessoa):
    """atualiza um usuario no banco de dados"""
    if bd.search(usuario.CPF == cpf):
        bd.remove(usuario.CPF==cpf)
        inserir(model)
    else:
        print('Usuario nao encontrado')