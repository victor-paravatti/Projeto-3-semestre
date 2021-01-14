from django.db import models


class Cliente(models.Model):
    cpf = models.CharField(max_length=12)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    endereco = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=150)
    cep = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.cpf

    class Meta:
        verbose_name_plural = 'Clientes'


class Pedido(models.Model):
    numero = models.CharField(max_length=10)
    datentrega = models.CharField(max_length=8)
    datpedido = models.CharField(max_length=8, blank=True, null=True)
    valorTotal = models.DecimalField(max_digits=10, decimal_places=0)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    id_funcionario = models.ForeignKey('Funcionario', on_delete=models.CASCADE)
    id_pagamento = models.ForeignKey('Pagamento', on_delete=models.CASCADE)
    id_status = models.ForeignKey('Status', on_delete=models.CASCADE)

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name_plural = 'Pedidos'


class Pagamento(models.Model):
    codigo = models.DecimalField(max_digits=10, decimal_places=0)
    metodo = models.CharField(max_length=45)

    def __str__(self):
        return self.metodo

    class Meta:
        verbose_name_plural = 'Pagamentos'


class Solicitacao(models.Model):
    codigo = models.DecimalField(max_digits=10, decimal_places=0)
    descricao = models.CharField(max_length=200)
    id_pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    id_status = models.ForeignKey('Status', on_delete=models.CASCADE)
    id_tipoSolicitacao = models.ForeignKey('TipoSolicitacao', on_delete=models.CASCADE)
    id_funcionario = models.ForeignKey('Funcionario', on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = 'Solicitações'


class TipoSolicitacao(models.Model):
    codigo = models.DecimalField(max_digits=10, decimal_places=0)
    tipo_solicitacao = models.CharField(max_length=45)            

    def __str__(self):
        return self.tipo_solicitacao

    class Meta:
        verbose_name_plural = 'Tipos de Solicitações'


class Status(models.Model):
    codigo = models.DecimalField(max_digits=10, decimal_places=0)
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Status'            


class Carrrinho(models.Model):
    codigo = models.DecimalField(max_digits=10, decimal_places=0)
    id_pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Carrinhos'


class ItensPedido(models.Model):
    sequencia_pedido = models.DecimalField(max_digits=10, decimal_places=0)
    quantidade_itens = models.DecimalField(max_digits=10, decimal_places=0)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=0)
    valor_total = models.DecimalField(max_digits=10, decimal_places=0)
    id_pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    id_produto = models.ForeignKey('Produto', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Itens Pedidos'


class Funcionario(models.Model):
    matricula = models.CharField(max_length=8)
    nome = models.CharField(max_length=45)
    email = models.CharField(max_length=60)
    telefone = models.CharField(max_length=11)
    senha = models.CharField(max_length=45)
    id_cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)
    id_setor = models.ForeignKey('Setor', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Funcionários'                           


class Cargo(models.Model):
    codigo = models.DecimalField(max_digits=10, decimal_places=0)
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Cargos'   


class Setor(models.Model):
    codigo = models.DecimalField(max_digits=10, decimal_places=0)
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Setores'


class Produto(models.Model):
    codigo = models.DecimalField(max_digits=10, decimal_places=0)
    titulo = models.CharField(max_length=45)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    escala = models.CharField(max_length=45)
    lote = models.DecimalField(max_digits=10, decimal_places=0)
    descricao = models.CharField(max_length=300)
    quantidade_disponivel = models.DecimalField(max_digits=10, decimal_places=0)
    unidades_vendidas = models.DecimalField(max_digits=10, decimal_places=0)
    foto = models.ImageField(upload_to='fotos_produtos', null=True)
    id_funcionario = models.ForeignKey('Funcionario', on_delete=models.CASCADE)
    id_fabricante = models.ForeignKey('Fabricante', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'Produtos'


class Fabricante(models.Model):
    codigo = models.DecimalField(max_digits=10, decimal_places=0)
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Fabricantes'


@property
def shipping(self):
	shipping = False
	orderitems = self.orderitem_set.all()
	for i in orderitems:
		if i.product.digital == False:
			shipping = True
	return shipping


@property
def get_cart_total(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.get_total for item in orderitems])
    return total 


@property
def get_cart_items(self):
	orderitems = self.orderitem_set.all()
	total = sum([item.quantity for item in orderitems])
	return total 

@property
def get_total(self):
	total = self.product.price * self.quantity
	return total

