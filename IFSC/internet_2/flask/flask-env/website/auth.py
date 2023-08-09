# logica de login de usuario
from flask import Blueprint, render_template, request, flash # type: ignore

auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET', 'POST']) # type: ignore
def login():
    if request.method == 'POST':
        return request.form.get('email')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        senha_2 = request.form.get('senha_2')
        
        if len(email) < 4:
            flash ('Email deve ser maior que 4 caracteres.', category='error')
        elif len(nome) < 2:
            flash ('Nome deve ser maior que 2 caracteres.', category='error')
        elif senha != senha_2:
            flash ('Senhas não são iguais.', category='error')
        elif len(senha) < 7:
            flash ('Senha deve ser maior que 7 caracteres.', category='error')
        else:
            flash ('Conta criada com sucesso!', category='success')
            # add user to database
            # redirect to home page

    #     return f"""
    #     email: {request.form.get('email')} <br/>
    #     nome: {request.form.get('nome')} <br/>
    #     senha: {request.form.get('senha')} <br/>
    #     confirma a senha: {request.form.get('senha_2')} <br/>
    # """
    
    return render_template("sign_up.html")