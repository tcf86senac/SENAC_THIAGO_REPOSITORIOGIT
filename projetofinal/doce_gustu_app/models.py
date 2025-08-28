# doce_gustu_app/models.py

from django.db import models
from django.contrib.auth.models import User

# O modelo 'Doce' representa um doce no menu.
class Doce(models.Model):
    # O nome do doce, limitado a 200 caracteres.
    nome = models.CharField(max_length=200)
    # Uma breve descrição do doce.
    descricao = models.TextField()
    # O preço do doce, com duas casas decimais.
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    # Um campo para a imagem do doce. O upload será feito para a pasta 'doces/'.
    foto = models.ImageField(upload_to='doces/')

    # O método __str__ é a representação em string do objeto, útil no admin.
    def __str__(self):
        return self.nome

    # A classe Meta é usada para adicionar metadados ao modelo,
    # como a ordenação. Aqui, ordenamos por nome.
    class Meta:
        ordering = ['nome']
        verbose_name_plural = "Doces" # Nome que aparece no painel de administração

# O modelo 'Salgado' representa um salgado no menu.
class Salgado(models.Model):
    # O nome do salgado.
    nome = models.CharField(max_length=200)
    # A descrição.
    descricao = models.TextField()
    # O preço do salgado.
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    # Um campo para a imagem do salgado. O upload será feito para a pasta 'salgados/'.
    foto = models.ImageField(upload_to='salgados/')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name_plural = "Salgados"

# O modelo 'Bebida' representa uma bebida no menu.
class Bebida(models.Model):
    # O nome da bebida.
    nome = models.CharField(max_length=200)
    # A descrição.
    descricao = models.TextField()
    # O preço da bebida.
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    # Um campo para a imagem da bebida. O upload será feito para a pasta 'bebidas/'.
    foto = models.ImageField(upload_to='bebidas/')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name_plural = "Bebidas"

# O modelo 'Cliente' armazena informações adicionais do usuário.
# Ele se relaciona com o modelo de usuário padrão do Django, que cuida da autenticação.
class Cliente(models.Model):
    # Relacionamento um-para-um com o modelo de usuário do Django.
    # Quando o usuário é deletado, o perfil do cliente também é.
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # Nome do cliente.
    nome = models.CharField(max_length=100)
    # Sobrenome do cliente.
    sobrenome = models.CharField(max_length=100)
    # Número de telefone do cliente.
    telefone = models.CharField(max_length=20)
    # Endereço de entrega do cliente.
    endereco_entrega = models.CharField(max_length=255)
    # Ponto de referência para a entrega.
    ponto_referencia = models.CharField(max_length=255, blank=True, null=True)
    # Campo para observações adicionais.
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        # Retorna o nome completo do cliente.
        return f"{self.nome} {self.sobrenome}"