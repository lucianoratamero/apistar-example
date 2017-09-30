
from django.db import models


class Produto(models.Model):
    nota = models.PositiveSmallIntegerField()
    nome = models.CharField(max_length=100)
    tamanho = models.CharField(max_length=100)
