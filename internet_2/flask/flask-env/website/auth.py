# logica de login de usuario
from flask import Blueprint, render_template, request

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
        return f"""
        email: {request.form.get('email')} <br/>
        nome: {request.form.get('nome')} <br/>
        senha: {request.form.get('senha')} <br/>
        confirma a senha: {request.form.get('senha_2')} <br/>
    """
    
    return render_template("sign_up.html")