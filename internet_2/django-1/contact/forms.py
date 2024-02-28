from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm # para criar um novo usuário
from django.contrib.auth.models import User # para criar um novo usuário

from . import models

class ContactForm(forms.ModelForm):
    class Meta: # variavel generica para lidar com dados em BD
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone', 
            'email', 'description', 'category'
        )
        widgets = { # dicionario do Python que serve como um array associativo
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Digite seu primeiro nome',
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Digite seu sobrenome',
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Digite seu telefone',
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Digite seu email',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Descreva sobre o Cliente',
                'class': 'form-control'
            }),
        }

#  herda de UserCreationForm. UserCreationForm é um formulário embutido do Django para registro de usuários.
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code='invalid')
            )

        return email
    
# email = self.cleaned_data.get('email'): Obtém o valor limpo do campo email.
# if User.objects.filter(email=email).exists():: Verifica se um usuário com o mesmo e-mail já existe no banco de dados.
# self.add_error('email', ValidationError('Já existe este e-mail', code='invalid')): Se um usuário com o mesmo e-mail existir, um erro é adicionado ao campo email, gerando um erro de validação.
# return email: O e-mail limpo é retornado, permitindo que o processamento do formulário continue até ser concluida