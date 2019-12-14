from django.db import models

# Create your models here.

class pessoas(models.Model):
    nome = models.TextField(max_length=200)
    endereco = models.TextField(max_length=200)
    altura = models.TextField(max_length=5)
    peso = models.TextField(max_length=5)
    imc = models.TextField(max_length=15)
