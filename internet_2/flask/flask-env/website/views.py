from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

# chamando
@views.route('/') #rota da pagina home, a rota é a barra, pois é a pagina principal 
@login_required # para acessar a pagina home, o usuario precisa estar logado
def home():
    return render_template("home.html") # renderizando a pagina home.html, que esta na pasta templates, o flask sabe que esta na pasta templates, pois é o padrão do flask