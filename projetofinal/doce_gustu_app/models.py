from django.db import models

class Item(models.Model):
    """
    Este modelo representa um item genérico.
    """
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Produto(models.Model):
    """
    Este modelo representa um produto que será exibido no cardápio.
    O campo 'imagem' foi alterado para armazenar uma URL.
    """
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Campo para armazenar a URL da imagem
    # Você pode usar URLs como "https://www.exemplo.com/cafe.jpg"
    imagem_url = models.CharField(max_length=500, default='https://placehold.co/600x400/000000/FFFFFF?text=Sem+Imagem')
    
    # Campo booleano para destacar o produto na página inicial
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
