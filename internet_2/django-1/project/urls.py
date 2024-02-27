from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static # para adicionar imagens no site _> linha 14 
from django.conf import settings # trazendo os arquivos de configuração do settings.py base statics e media 

urlpatterns = [
    path('', include('contact.urls')), # enviando para o arquivo contact/urls.py 
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns padrao do django para alterar o caminho para os arquivos estaticos e imagens
# += para adicionar mais caminhos pois o django não reconhece o caminho padrão para os arquivos estaticos e imagens
# static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # é necessário para adicionar imagens no site
#  linha basicamente diz: "Inclua padrões de URL para servir arquivos de mídia e use a URL base especificada (MEDIA_URL) 
# e o caminho do sistema de arquivos local (MEDIA_ROOT)."

# https://docs.djangoproject.com/pt-br/4.2/howto/static-files/