from django.shortcuts import render
from .models import Produto

# View para a página inicial (Home)
def home(request):
    """
    Renderiza a página inicial (index.html), buscando e exibindo
    produtos em destaque e os 3 primeiros produtos de cada categoria.
    """
    try:
        # Filtra os produtos que foram marcados como destaque no painel do administrador.
        produtos_destaque = Produto.objects.filter(destaque=True)
    except Exception as e:
        print(f"Erro ao buscar produtos de destaque: {e}")
        produtos_destaque = []

    try:
        # Consulta os 3 primeiros produtos da categoria 'Doce'
        doces = Produto.objects.filter(categoria='Doce')[:3]

        # Consulta os 3 primeiros produtos da categoria 'Salgado'
        salgados = Produto.objects.filter(categoria='Salgado')[:3]

        # Consulta os 3 primeiros produtos da categoria 'Bebida'
        bebidas = Produto.objects.filter(categoria='Bebida')[:3]
    except Exception as e:
        print(f"Erro ao buscar produtos por categoria: {e}")
        doces = []
        salgados = []
        bebidas = []

    # Cria um dicionário (contexto) com todos os dados que serão enviados para o template.
    contexto = {
        'produtos_destaque': produtos_destaque,
        'doces': doces,
        'salgados': salgados,
        'bebidas': bebidas,
    }

    # Renderiza o template 'index.html' e passa o dicionário de contexto.
    return render(request, 'index.html', contexto)

# View para a página de carrinho
def carrinho(request):
    """
    Renderiza a página do carrinho (carrinho.html).
    """
    return render(request, 'carrinho.html')

# View para a página de cadastro de cliente
def cliente_cadastro(request):
    """
    Renderiza a página de cadastro de cliente (cliente_cadastro.html).
    """
    return render(request, 'cliente_cadastro.html')

# View para a página do cliente logado
def cliente_logado(request):
    """
    Renderiza a página do cliente logado (cliente_logado.html).
    """
    return render(request, 'cliente_logado.html')

# View para a página de detalhes de um produto
def produto(request):
    """
    Renderiza a página de detalhes do produto (produto.html).
    Esta view precisará ser aprimorada para exibir um produto específico no futuro.
    """
    return render(request, 'produto.html')
