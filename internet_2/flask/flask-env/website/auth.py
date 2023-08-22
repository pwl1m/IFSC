# logica de login de usuario
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user

from website import db
from .models import Usuario

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email=request.form.get('email') 
        senha=request.form.get('senha')

        usuario = Usuario.query.filter_by(email=email).first() # email é a classe e depois o email do request - o first é para pegar o primeiro usuario que encontrar 

        if usuario:
            if check_password_hash (usuario.senha, senha): # verifica se a senha do usuario é igual a senha do banco de dados, se for igual loga
                flash ('Logado!', category='success') 
                login_user(usuario, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Senha incorreta, tente novamente.', category='error')
        else:
            flash('Email não existe.', category='error')

    return render_template("login.html")

@auth.route('/logout') 
def logout():
    logout_user() # função do flask_login para deslogar o usuario
    return redirect(url_for('auth.login')) # redireciona para a pagina de login

@auth.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        
        email = request.form.get('email')
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        senha_2 = request.form.get('senha_2')

        usuario = Usuario.query.filter_by(email=email).first() # email é a classe e depois o email do request - o first é para pegar o primeiro usuario que encontrar
        if usuario:
        elif len(email) < 4:
            flash('Email deve ser maior que 4 caracteres.', category='error')
        elif len(nome) < 2:
            flash('Nome deve ser maior que 2 caracteres.', category='error')
        elif senha != senha_2:
            flash('Senhas não são iguais.', category='error')
        elif len(senha) < 7:
            flash('Senha deve ser maior que 7 caracteres.', category='error')
        else:
            usuario = Usuario(email=email, nome=nome, senha=generate_password_hash(senha,method='sha256')) # cria usuario com senha criptografada 
            
            db.session.add(usuario) # adiciona usuario no banco de dados 
            db.session.commit() # salva usuario no banco de dados
            login_user(usuario, remember=True) # loga usuario, remember=True para manter logado
            flash('Conta criada com sucesso!', category='success') # mensagem de sucesso, category='success' para mensagem verde
            return redirect(url_for('views.home')) # redireciona para pagina home

    return render_template("sign_up.html")