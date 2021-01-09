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
        return self.nome + '(' + str(self.id) + ')'

    class Meta:
        verbose_name_plural = 'Clientes'


class Pedido(models.Model):
    numero = models.CharField(max_length=10)
    datentrega = models.CharField(max_length=8)
    datpedido = models.CharField(max_length=8, blank=True, null=True)
    valor


    def __str__(self):
        return self.nome + '(' + str(self.id) + ')'

    class Meta:
        verbose_name_plural = 'Pedidos'




    




