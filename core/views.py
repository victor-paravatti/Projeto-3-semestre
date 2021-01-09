from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'core/index.html')


@login_required
def carrinho(request):
    data = cartData(request)
    carrinhoItems = data['carrinhoItems']
    compra = data['compra']
    items = data['items']
    contexto = {'items':items, 'compra':compra, 'carrinhoItems':carrinhoItems}

    return render(request, "core/carrinho.html", contexto)


@login_required
def login(request):
    return render(request, 'core/login.html')


    