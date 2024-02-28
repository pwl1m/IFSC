from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'), # raiz do site 
    path('search/', views.search, name='search'), 
    
    path('<int:contact_id>/', views.contact, name='contact'), # parametro para o id do contato 
    path('contact/create/', views.create, name='create'), # criação de um novo contato
    path('<int:contact_id>/update/', views.update, name='update'), # Este é um nome de variável que captura o valor inteiro da URL. que no caso é o numero do ID
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'), # deletar um contato existente
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),    
]
