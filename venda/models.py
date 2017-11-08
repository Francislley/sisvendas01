from django.db import models
from django.contrib.auth.models import User


class Produto(models.Model):
    
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    
    usuario = models.ForeignKey(User)
    valor = models.FloatField()
    data_compra = models.DateField()
    produto = models.ForeignKey(Produto)


class Pagamento(models.Model):

    valor = models.FloatField()
    usuario = models.ForeignKey(User)
    data_pagamento = models.DateField()

