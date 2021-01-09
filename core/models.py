from typing import Tuple
from django.db import models

class Cliente(models.Model):
    cpf = models.CharField(max_length=12)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    endereco= models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=150)
    cep = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.cpf + '(' + str(self.id) + ')'

    class Meta:
        verbose_name_plural = 'Clientes'


class Pedido(models.Model):
    numero = models.CharField(max_length=10)
    datentrega = models.CharField(max_length=8)
    datpedido = models.CharField(max_length=8, blank=True, null=True)
    valorTotal = models.DecimalField(max_digitis=10, decimal_places=6)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    id_funcionario = models.ForeignKey('Funcionario', on_delete=models.CASCADE)
    id_pagamento = models.ForeignKey('Pagamento', on_delete=models.CASCADE)
    id_status = models.ForeingKey('Status', on_delete=models.CASCADE)


    def __str__(self):
        return self.numero + '(' + str(self.id) + ')'

    class Meta:
        verbose_name_plural = 'Pedidos'


class Pagamento(models.Model):
    codigo = models.DecimalField(max_digitis=10, decimal_places=6)
    metodo = models.CharField(max_length=45)

    def __str__(self):
        return self.codigo + '(' + str(self.id) + ')'

    class Meta:
        verbose_name_plural = 'Pagamentos'

class Solicitacao(models.Model):
    codigo = models.DecimalField(max_digitis=10, decimal_places=6)
    descricao = models.CharField(max_length=200)
    id_pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    id_status = models.ForeignKey('Status', on_delete=models.CASCADE)
    id_tipoSolicitacao = models.ForeignKey('TipoSolicitacao', on_delete=models.CASCADE)
    id_funcionario = models.ForeignKey('Funcionario', on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo + '(' + str(self.id) + ')'

    class Meta:
        verbose_name_plural = 'Solicitações'

class TipoSolicitacao(models.Model):
    codigo = models.DecimalField(max_digitis=10, decimal_places=6)
    tipo_solicitacao = models.CharField(max_length=45)            

    def __str__
