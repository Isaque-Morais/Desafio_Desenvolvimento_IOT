from django.db import models
from .tipo_nota import tipo_nota

class Nota(models.Model):
    numero = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    mercado = models.DateField()
    valor_compra = models.DateField()
    data = models.DateField()
    entidade = models.CharField(max_length=100)
    tipos_notas = models.TextField(choices=tipo_nota.choices, max_length=4, default=0)