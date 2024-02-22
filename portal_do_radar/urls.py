# Seu arquivo principal urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Importe a view 'index' do diretório do projeto

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('yt/', include('videos_youtube.urls')),
    path('', include('noticias.urls')),
   

]

# Adicione a configuração para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
