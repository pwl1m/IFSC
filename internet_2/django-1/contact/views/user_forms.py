from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm # para fazer o login 
from django.shortcuts import redirect, render

from contact.forms import RegisterForm # importa o formulario de registro 

def register(request):
    form = RegisterForm()
    
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid(): # solucao copilot para o erro 
            form.save()
            return redirect('contact:login')
    
    return render( # renderiza a pagina de registro
        request,  # request é o objeto que o django recebe quando alguem acessa uma pagina
        'contact/register.html', # o segundo parametro é o nome do template
        {
        'form': form, # dicionario com as variaveis que o template vai usar
        }
    )
        
    
def login_view(request):
    form = AuthenticationForm(request) # formulario de autenticacao do django

    if request.method == 'POST': # se o metodo for POST
        form = AuthenticationForm(request, data=request.POST) # cria o formulario de autenticacao _> linha 37

        if form.is_valid():
            user = form.get_user() # nao é repsonsavel por logar, mas se ta tudo correto com os dados do usuario
            auth.login(request, user) # loga o usuario 
            messages.success(request, 'Logado com sucesso!')
            return redirect('contact:index') # a funcao para aqui caso nao
        messages.error(request, 'Login inválido') # caso nao, vou retornar uma mensagem de erro e entao renderizar a pagina de login novamente

    return render( # renderiza a pagina de login
        request,
        'contact/login.html',
        {
            'form': form
        }
    )

def logout_view(request): # funcao para deslogar
    auth.logout(request) 
    return redirect('contact:login') # redireciona para a pagina de login