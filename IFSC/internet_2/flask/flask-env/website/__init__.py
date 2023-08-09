from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secreto'

# blueprint é uma estrategia para organizar melhor os seus modulos, inspirada do django, em apps, cada app é um modulo que pode ser reutilizado em outros projetos
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app