from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.forms import *

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


@login_required
def cadastro(request):
    form = FormCliente(request.POST or None)
    contexto = {'form': form, 'acao': 'Cadastro de Cliente', 'titulo': 'Cadastar'}
    if form.is_valid():
        form.save()
        return redirect('url_login')
    else:        
        return render(request, "core/cadastro.html", contexto)

    