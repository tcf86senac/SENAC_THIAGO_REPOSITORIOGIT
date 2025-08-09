from django.db import models

# Create your models here.
class Produto(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.URLField(max_length=300)



