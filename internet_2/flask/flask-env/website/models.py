from . import db #variavel db que foi criada no __init__.py
from sqlalchemy.sql import func
from flask_login import UserMixin

# criando a tabela de usuario
class Usuario(db.Model, UserMixin): #UserMixin é uma classe que tem metodos que o flask_login precisa para funcionar
    # criando as colunas da tabela
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    nome = db.Column(db.String(150))
    senha = db.Column(db.String(150))
    notas = db.relationship('Nota') #criando o relacionamento com a tabela nota, o usuario vai ter varias notas, o parametro 'Nota' é o nome da tabela, se fosse o nome da classe seria 'Nota()'

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(1000))
    data = db.Column(db.DateTime(timezone=True), default=func.now()) #func.now() é uma função do sqlalchemy que pega a data e hora atual
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id')) #criando a chave estrangeira, o usuario_id vai ser a chave primaria da tabela usuario