from django.shortcuts import render
from .models import Produto

# Create your views here.
def home(request):
    return render(request, 'index.html')

def carrinho(request):
    return render(request, 'carrinho.html')

def cliente_cadastro(request):
    return render(request, 'cliente_cadastro.html')

def cliente_logado(request):
    return render(request, 'cliente_logado.html')

def produto(request):
    return render(request, 'produto.html')

def home(request):
    # Pega os produtos que você marcou como "destaque" no painel de administração
    produtos_destaque = Produto.objects.filter(destaque=True)

    # Prepara uma caixa de presentes com os produtos para enviar ao HTML
    contexto = {
        'produtos_destaque': produtos_destaque
    }

    # Entrega a caixa de presentes para o seu arquivo 'home.html'
    return render(request, 'index.html', contexto)