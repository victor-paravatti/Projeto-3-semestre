from django.contrib import admin
from django.urls import path, include
from core.views import home, carrinho, login, cadastro, listagem_produto
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('', home, name='url_home'),
    path('carrinho/', carrinho, name='url_carrinho'),
    path('login/', login, name='url_login'),
    path('cadastro/', cadastro, name='url_cadastro'),
    path('listagem_produto/', listagem_produto, name='url_listagem_produto')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)