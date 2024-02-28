from django.contrib import admin
from contact import models


# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 
    ordering = 'id',
    list_filter = 'created_date', # para filtrar por data de criação
    search_fields = 'first_name', 'last_name', 'phone',
    list_per_page = 10 # para mostrar 10 contatos por página
    list_max_show_all = 100 # para mostrar 100 no maximo por página
    # list_editable _> para editar na pag principal do admin
    
# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', 
    ordering = 'id',