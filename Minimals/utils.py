import json
from core.models import Cliente, Produto

def cookieCart(request):

	#Create empty cart for now for non-logged in user
	try:
		carrinho = json.loads(request.COOKIES['carrinho'])
	except:
		carrinho = {}
		print('CARINHO:', carrinho)

	items = []
	order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
	cartItems = order['get_cart_items']

	for i in carrinho:
		#We use try block to prevent items in cart that may have been removed from causing error
		try:
			cartItems += car[i]['quantity']

			produto = Produtos.objects.get(id=i)
			total = (produto.price * cart[i]['quantity'])

			order['get_cart_total'] += total
			order['get_cart_items'] += cart[i]['quantity']

			item = {
				'id':produto.id,
				'product':{'id':produto.id,'name':produto.name, 'price':produto.price, 
				'imageURL':produto.imageURL}, 'quantity':cart[i]['quantity'],
				'digital':produto.digital,'get_total':total,
				}
			items.append(item)

			if produto.digital == False:
				order['shipping'] = True
		except:
			pass
			
	return {'cartItems':cartItems ,'order':order, 'items':items}

def cartData(request):
	if request.user.is_authenticated:
		cliente = request.user.Ciente
		order, created = Order.objects.get_or_create(cliente=Cliente, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		cookieData = cookieCart(request)
		cartItems = cookieData['cartItems']
		order = cookieData['order']
		items = cookieData['items']

	return {'cartItems':cartItems ,'order':order, 'items':items}

	
def guestOrder(request, data):
	name = data['form']['nome']
	email = data['form']['email']

	cookieData = cookieCart(request)
	items = cookieData['items']

	cliente, created = Cliente.objects.get_or_create(
			email=email,
			)
	Cliente.name = name
	Cliente.save()

	order = Order.objects.create(
		cliente=Cliente,
		complete=False,
		)

	for item in items:
		product = Produto.objects.get(id=item['id'])
		orderItem = OrderItem.objects.create(
			Produto=product,
			order=order,
			quantity=item['quantity'],
		)
	return cliente, order

