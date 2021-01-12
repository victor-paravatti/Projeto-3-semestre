from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from core.models import Produto,Cliente
from core.forms import FormCliente, FormProduto
from Minimals.utils import cookieCart, cartData, guestOrder
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
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'core/carrinho.html', context)


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


def updateItem(request):
	data = json.loads(request.body)
	produtoId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', produtoId)

	Cliente = request.user.customer
	produto = Produto.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, produto=Produto)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		cliente = request.user.Cliente
		order, created = Order.objects.get_or_create(cliente=Cliente, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)


