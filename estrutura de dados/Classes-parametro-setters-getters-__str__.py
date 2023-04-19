# Crie uma classe Usuário com os atributos id, nome, cpf, endereço, email, telefone e senha.
# Defina construtor com parâmetros, métodos setters, getters e __str__

import csv
import os

def cadastrar_cliente():
  dados = {}
  id = input ("id")
  nome = input("Nome")
  cpf  = input("CPF")
  endereco = input ("endereco")
  email = input("email")
  senha = input("senha")
 
  dados[id] = [nome, cpf, endereco, email,senha]
 
  colunas = ['nome','cpf', 'nome', 'endereco','email']
  file_exists = os.path.isfile('clientes.csv')
  with open('clientes.csv', 'a', newline='') as clientes_csv:
    cadastrar = csv.DictWriter(clientes_csv, fieldnames=colunas, delimiter=';', lineterminator='\r\n')
    if not file_exists:
        cadastrar.writeheader()
    cadastrar.writerow({'cpf':cpf, 'nome':nome.title()})
 
  print('Cadastro realizado com sucesso!')

def cadastrar_titulo():
  os.system('cls') or None
  print('\n CADASTRO de Titulos \n')
  cadastro = {}
  id               = input("Id")
  nome             = input("Nome")
  ano              = input("ano")
  duracao          = input("duracao")
  diaria           = input("diaria")
  
  cadastro[id] = [nome, ano, duracao, diaria] # Salva os dados em um dicionário
  
  filmes_csv = open("filmes.csv","a")
  filmes_csv.write(f"{id};{nome.upper()};{nome.title()}")
  filmes_csv.close()

def cadastrar_Artista():
  os.system('cls') or None
  print('\n CADASTRO de Artista \n')
  cadastro = {}
  id               = input("Id")
  nome             = input("Nome")
  seguidores       = input("seguidores")
  
  cadastro[id] = [id,nome,seguidores] # Salva os dados em um dicionário
  
  filmes_csv = open("filmes.csv","a")
  filmes_csv.write(f"{id};{nome.upper()};{nome.title()}")
  filmes_csv.close()

def locacao():
  os.system('cls') or None
  print('\nlocacao\n')	
  cadastro = {}
  id               = input("id")
  cliente          = input("cliente")
  titulo           = input("titulo")
  dias             = input("dias")
  forma_pagamento  = input("forma de pagamento")
 
  cadastro = {'nome_usuario':nome_usuario.title(), 'codigo_filme':codigo_filme, 'data_emprestimo':data_emprestimo}
  emprestimos_csv = open("emprestimos.csv","a")
  emprestimos_csv.write(f"{nome_usuario};{codigo_filme};{data_emprestimo}\n")
  emprestimos_csv.close()
#adicionar valor da locacao

