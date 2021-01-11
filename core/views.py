from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.forms import FormCliente
from core.models import Produto

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



def login(request):
    return render(request, 'core/login.html')



def cadastro(request):
    form = FormCliente(request.POST or None)
    contexto = {'form': form, 'acao': 'Cadastro de Cliente', 'titulo': 'Cadastar'}
    if form.is_valid():
        form.save()
        return redirect('url_login')
    else:        
        return render(request, "core/cadastro.html", contexto)


def listagem_produto(request):
    produto = Produto.objects.all()
    contexto = {'produtos': produtos}
    return render(request, "core/index.html", contexto)

    