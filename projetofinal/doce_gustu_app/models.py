from django.db import models

# Create your models here.
from django.db import models

class Item(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.nome