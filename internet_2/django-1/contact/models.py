from django.db import models
from django.utils import timezone # para salvar a data e hora atual do contato no bd



class Category (models.Model):
    class Meta:
        verbose_name = 'Category' # para mudar o nome da categoria no admin
    
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name


# criar, buscar, atualizar e deletar os contatos no banco de dados 
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now) # para salvar a data e hora atual do contato no bd 
    description = models.TextField(blank=True)
    # criar bairro = verificar migrations e admin.py 
    # para adicionar bairros específicos, verificar migrations e admin.py
    # bairro = models.CharField(max_length=50, choices=BAIRROS_CHOICES)
    # BAIRROS_CHOICES = [
    #     ('1', 'Centro'),
    #     ('2', 'Vila Nova'),

    # ]
    # criar endereço
    # endereço = models.CharField(max_length=50, choices=ENDEREÇO_CHOICES)
    show = models.BooleanField(default=True) # para mostrar ou não o contato na lista de contatos
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/') # para adicionar uma foto ao contato y = ano, m = mês, d = dia
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, # para não apagar o contato caso a categoria seja deletada 
        blank=True, null=True # para não ser obrigatório selecionar uma categoria E para não apagar o contato caso a categoria seja deletada
    )
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'