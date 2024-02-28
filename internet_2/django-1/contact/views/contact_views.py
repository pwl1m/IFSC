# Importe os módulos e classes necessários do Django
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render # get_object_or_404 para retornar 404 caso o contato não exista
from django.core.paginator import Paginator # para paginação dos contatos

from contact.models import Contact

def index(request):
    # Recupere uma lista de contatos com show=True, ordenados por id em ordem decrescente, e selecione uma fatia [10:20]
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')
    paginator = Paginator(contacts, 10) # 10 contatos por página
    page_number = request.GET.get('page') # recupera o número da página
    page_obj = paginator.get_page(page_number) # recupera os contatos da página

    # Criar um dicionário contendo os contatos e o site_title
    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }

    # Renderize o modelo index.html com o contexto especificado
    return render(
        request,
        'contact/index.html',
        context
    )

# Defina uma função de visualização para pesquisar contatos
def search(request):
    # Obtenha o valor de pesquisa dos parâmetros GET, removendo espaços em branco no início e no final
    search_value = request.GET.get('q', '').strip() # strip para remover os espaços em branco dentro da string

    # Se o valor de pesquisa estiver vazio, redirecione para a página inicial
    if search_value == '':
        return redirect('contact:index') 

    # Filtrar os contatos com base nos critérios de pesquisa (nome, sobrenome, telefone ou e-mail)
    # icontains para ignorar se a pesquisa for maiuscula ou minuscula e o __ para indicar que é um campo do banco de dados 
    contacts = Contact.objects \
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')
        
    paginator = Paginator(contacts, 10) # 10 contatos por página
    page_number = request.GET.get('page') # recupera o número da página
    page_obj = paginator.get_page(page_number) # recupera os contatos da página

    # dicionário de contexto contendo os resultados da pesquisa e o site_title
    context = {
        'page_obj': page_obj,
        'site_title': 'Pesquisa - ',
        'search_value': search_value,
    }

    # Renderizar o modelo index.html com o contexto especificado
    return render(
        request,
        'contact/index.html',
        context
    )

# função para exibir um único contato
def contact(request, contact_id):
    # retornar um único contato com o ID especificado e show=True ou retorne uma resposta 404
    single_contact = get_object_or_404( # exclusivo do django para retornar 404 caso o contato não exista
        Contact, pk=contact_id, show=True # show=True para mostrar apenas os contatos que estão marcados como True (relacionado na criação do contato pelo admin)
    )

    # Criar título do site com  nome e sobrenome do contato
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    # dicionário contendo o contato e o site_title
    context = {
        'contact': single_contact,
        'site_title': site_title
    }

    return render(
        request,
        'contact/contact.html',
        context
    )
