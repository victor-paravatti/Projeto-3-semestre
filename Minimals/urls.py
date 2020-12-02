from django.contrib import admin
from django.urls import path
from core.views import home, carrinho, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('carrinho/', carrinho, name='url_carrinho'),
    path('login/', login, name='url_login')
]
