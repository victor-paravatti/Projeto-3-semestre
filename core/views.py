from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from core.models import Produto, Funcionario, Cliente
from core.forms import FormCliente, FormProduto, FormFuncionario
from django.http import JsonResponse
import json
import datetime


def home(request):
    produto = Produto.objects.all()
    contexto = {'produtos': produto}
    return render(request, 'core/index.html', contexto)


class Cadastrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/cadastrar.html'



def carinho(request):
	return render(request, 'core/carrinho.html')


def cadastrar_cliente(request):
    form = FormCliente(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastrar Cliente', 'titulo': 'Cadastro'}
    if form.is_valid():
        form.save()
        return redirect('url_listagem_clientes')
    else:
        return render(request, "core/cadastrar_cliente.html", contexto)


def cadastrar_produto(request):
    form = FormProduto(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastar Produto'}
    if form.is_valid():
        form.save()
        return redirect('url_listar_produto')
    else:
        return render(request, "core/cadastrar_produto.html", contexto)


def listar_produto(request):
    if request.POST:
        if request.POST['codigo']:
            produtos = Produto.objects.filter(codigo=request.POST['codigo'])
        else:
            produtos = Produto.objects.all()
    else:
        produtos = Produto.objects.all()
    contexto = {'produtos': produtos}
    return render(request, "core/listar_produto.html", contexto)


def editar_produto(request, id):
    obj = Produto.objects.get(id=id)
    form = FormProduto(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('url_listar_produto')
    else:
        return render(request, 'core/cadastrar_produto.html', contexto)


def excluir_produto(request, id):
    obj = Produto.objects.get(id=id)
    contexto = {'acao': obj.codigo, 'redirect': '/listar_produto/'}
    if request.POST:
        obj.delete()
        return redirect('url_listar_produto')
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


def exibir_produto(request, id):
    produtos = Produto.objects.filter(id=id)
    contexto = {'produtos': produtos}
    return render(request, "core/exibir_produto.html", contexto)


def cadastrar_funcionario(request):
    form = FormFuncionario(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastar Funcionario'}
    if form.is_valid():
        form.save()
        return redirect('url_listar_funcionario')
    else:
        return render(request, "core/cadastrar_funcionario.html", contexto)


def listar_funcionario(request):
    if request.POST:
        if request.POST['matricula']:
            funcionarios = Funcionario.objects.filter(matricula=request.POST['matricula'])
        else:
            funcionarios = Funcionario.objects.all()
    else:
        funcionarios = Funcionario.objects.all()
    contexto = {'funcionarios': funcionarios}
    return render(request, "core/listar_funcionario.html", contexto)


def editar_funcionario(request, id):
    obj = Funcionario.objects.get(id=id)
    form = FormFuncionario(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('url_listar_funcionario')
    else:
        return render(request, 'core/cadastrar_funcionario.html', contexto)


def excluir_funcionario(request, id):
    obj = Funcionario.objects.get(id=id)
    contexto = {'acao': obj.matricula, 'redirect': '/listar_funcionario/'}
    if request.POST:
        obj.delete()
        return redirect('url_listar_funcionario')
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)
