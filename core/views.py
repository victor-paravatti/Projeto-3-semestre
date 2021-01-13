from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from core.models import Cliente, Produto, Funcionario, Cargo, Setor, Fabricante, Pagamento, \
    Status, TipoSolicitacao 
from core.forms import FormCliente, FormProduto, FormFuncionario, FormCargo, FormSetor, \
    FormFabricante, FormStatus, FormTipoSolicitacao, FormPagamento
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


def cadastrar_cargo(request):
    form = FormCargo(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastar Cargo'}
    if form.is_valid():
        form.save()
        return redirect('url_listar_cargo')
    else:
        return render(request, "core/cadastrar_cargo.html", contexto)


def listar_cargo(request):
    if request.POST:
        if request.POST['codigo']:
            cargos = Cargo.objects.filter(codigo=request.POST['codigo'])
        else:
            cargos = Cargo.objects.all()
    else:
        cargos = Cargo.objects.all()
    contexto = {'cargos': cargos}
    return render(request, "core/listar_cargo.html", contexto)


def editar_cargo(request, id):
    obj = Cargo.objects.get(id=id)
    form = FormCargo(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('url_listar_cargo')
    else:
        return render(request, 'core/cadastrar_cargo.html', contexto)


def excluir_cargo(request, id):
    obj = Cargo.objects.get(id=id)
    contexto = {'acao': obj.codigo, 'redirect': '/listar_cargo/'}
    if request.POST:
        obj.delete()
        return redirect('url_listar_cargo')
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


def cadastrar_setor(request):
    form = FormSetor(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastar Setor'}
    if form.is_valid():
        form.save()
        return redirect('url_listar_setor')
    else:
        return render(request, "core/cadastrar_setor.html", contexto)


def listar_setor(request):
    if request.POST:
        if request.POST['codigo']:
            setors = Setor.objects.filter(codigo=request.POST['codigo'])
        else:
            setors = Setor.objects.all()
    else:
        setors = Setor.objects.all()
    contexto = {'setors': setors}
    return render(request, "core/listar_setor.html", contexto)


def editar_setor(request, id):
    obj = Setor.objects.get(id=id)
    form = FormSetor(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('url_listar_setor')
    else:
        return render(request, 'core/cadastrar_setor.html', contexto)


def excluir_setor(request, id):
    obj = Setor.objects.get(id=id)
    contexto = {'acao': obj.codigo, 'redirect': '/listar_setor/'}
    if request.POST:
        obj.delete()
        return redirect('url_listar_setor')
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


def cadastrar_fabricante(request):
    form = FormFabricante(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastar Fabricante'}
    if form.is_valid():
        form.save()
        return redirect('url_listar_fabricante')
    else:
        return render(request, "core/cadastrar_fabricante.html", contexto)


def listar_fabricante(request):
    if request.POST:
        if request.POST['codigo']:
            fabricantes = Fabricante.objects.filter(codigo=request.POST['codigo'])
        else:
            fabricantes = Fabricante.objects.all()
    else:
        fabricantes = Fabricante.objects.all()
    contexto = {'fabricantes': fabricantes}
    return render(request, "core/listar_fabricante.html", contexto)


def editar_fabricante(request, id):
    obj = Fabricante.objects.get(id=id)
    form = FormFabricante(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('url_listar_fabricante')
    else:
        return render(request, 'core/cadastrar_fabricante.html', contexto)


def excluir_fabricante(request, id):
    obj = Fabricante.objects.get(id=id)
    contexto = {'acao': obj.codigo, 'redirect': '/listar_fabricante/'}
    if request.POST:
        obj.delete()
        return redirect('url_listar_fabricante')
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


def cadastrar_status(request):
    form = FormStatus(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastar Status'}
    if form.is_valid():
        form.save()
        return redirect('url_listar_status')
    else:
        return render(request, "core/cadastrar_status.html", contexto)


def listar_status(request):
    if request.POST:
        if request.POST['codigo']:
            statuss = Status.objects.filter(codigo=request.POST['codigo'])
        else:
            statuss = Status.objects.all()
    else:
        statuss = Status.objects.all()
    contexto = {'statuss': statuss}
    return render(request, "core/listar_status.html", contexto)


def editar_status(request, id):
    obj = Status.objects.get(id=id)
    form = FormStatus(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('url_listar_status')
    else:
        return render(request, 'core/cadastrar_status.html', contexto)


def excluir_status(request, id):
    obj = Status.objects.get(id=id)
    contexto = {'acao': obj.codigo, 'redirect': '/listar_status/'}
    if request.POST:
        obj.delete()
        return redirect('url_listar_status')
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


def cadastrar_tipo_solicitacao(request):
    form = FormTipoSolicitacao(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastar Tipo de Solicitação'}
    if form.is_valid():
        form.save()
        return redirect('url_listar_tipo_solicitacao')
    else:
        return render(request, "core/cadastrar_tipo_solicitacao.html", contexto)


def listar_tipo_solicitacao(request):
    if request.POST:
        if request.POST['codigo']:
            tipo_solicitacoes = TipoSolicitacao.objects.filter(codigo=request.POST['codigo'])
        else:
            tipo_solicitacoes = TipoSolicitacao.objects.all()
    else:
        tipo_solicitacoes = TipoSolicitacao.objects.all()
    contexto = {'tipo_solicitacoes': tipo_solicitacoes}
    return render(request, "core/listar_tipo_solicitacao.html", contexto)


def editar_tipo_solicitacao(request, id):
    obj = TipoSolicitacao.objects.get(id=id)
    form = FormTipoSolicitacao(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('url_listar_tipo_solicitacao')
    else:
        return render(request, 'core/cadastrar_tipo_solicitacao.html', contexto)


def excluir_tipo_solicitacao(request, id):
    obj = TipoSolicitacao.objects.get(id=id)
    contexto = {'acao': obj.codigo, 'redirect': '/listar_tipo_solicitacao/'}
    if request.POST:
        obj.delete()
        return redirect('url_listar_tipo_solicitacao')
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


def cadastrar_pagamento(request):
    form = FormPagamento(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastar Pagamento'}
    if form.is_valid():
        form.save()
        return redirect('url_listar_pagamento')
    else:
        return render(request, "core/cadastrar_pagamento.html", contexto)


def listar_pagamento(request):
    if request.POST:
        if request.POST['codigo']:
            pagamentos = Pagamento.objects.filter(codigo=request.POST['codigo'])
        else:
            pagamentos = Pagamento.objects.all()
    else:
        pagamentos = Pagamento.objects.all()
    contexto = {'pagamentos': pagamentos}
    return render(request, "core/listar_pagamento.html", contexto)


def editar_pagamento(request, id):
    obj = Pagamento.objects.get(id=id)
    form = FormPagamento(request.POST or None, request.FILES or None, instance=obj)
    contexto = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('url_listar_pagamento')
    else:
        return render(request, 'core/cadastrar_pagamento.html', contexto)


def excluir_pagamento(request, id):
    obj = Pagamento.objects.get(id=id)
    contexto = {'acao': obj.codigo, 'redirect': '/listar_pagamento/'}
    if request.POST:
        obj.delete()
        return redirect('url_listar_pagamento')
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)
