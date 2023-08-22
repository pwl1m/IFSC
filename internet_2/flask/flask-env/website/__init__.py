from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()
DB_NAME = "database.db"

def create_app():    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secreto'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # o banco vai ser no formato de arquivo sqlite
    db.init_app(app) #inicializando a engine com app

# blueprint é uma estrategia para organizar melhor os seus modulos, inspirada do django, em apps, cada app é um modulo que pode ser reutilizado em outros projeto
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') #url_prefix é o prefixo da url, ou seja, o que vem antes da rota, no caso, não tem nada, então é só uma barra, mas se fosse /auth, seria /auth/login 
    app.register_blueprint(auth, url_prefix='/')

    from .models import Usuario, Nota #importando os modelos, para que o banco de dados saiba que eles existem
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Faça o login para acessar essa página.' #mensagem que aparece quando o usuario tenta acessar uma pagina que precisa estar logado
    login_manager.init_app(app) #inicializando o login manager, passando o banco de dados como parametro para ele saber qual é o banco de dados que ele vai usar para fazer o login e o logout do usuario, e qual é a rota que ele vai redirecionar o usuario caso ele não esteja logado

    @login_manager.user_loader #para carregar o usuario, o id_usuario é o id do usuario que esta logado, o load_user é uma função que retorna o usuario
    def load_user(id):
        return Usuario.query.get(int(id))

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Banco de dados criado.')