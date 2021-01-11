from django.contrib import admin
from django.urls import path, include
from core.views import cadastrar, home, carrinho, login
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('', home, name='url_home'),
    path('carrinho/', carrinho, name='url_carrinho'),
    path('login/', login, name='url_login'),
    path('cadastrar/', cadastrar.as_view(), name='url_cadastrar')

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)