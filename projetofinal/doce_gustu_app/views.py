# DOCE_GUSTO/doce_gustu_app/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Doce, Salgado, Bebida, Cliente
from .forms import ClienteCadastroForm # O formulário para o cadastro

# View para a página inicial (Home)
def home(request):
    """
    Renderiza a página inicial (index.html), buscando e exibindo
    os produtos de cada categoria (doces, salgados, bebidas).
    """
    try:
        # Busca todos os produtos de cada categoria do banco de dados.
        doces = Doce.objects.all()
        salgados = Salgado.objects.all()
        bebidas = Bebida.objects.all()
    except Exception as e:
        # Em caso de erro, por exemplo, se o banco de dados não estiver configurado,
        # printa o erro e define as listas como vazias para evitar quebra.
        print(f"Erro ao buscar produtos: {e}")
        doces = []
        salgados = []
        bebidas = []

    # Cria um dicionário (contexto) com os dados que serão enviados para o template.
    contexto = {
        'doces': doces,
        'salgados': salgados,
        'bebidas': bebidas,
    }

    # Renderiza o template 'index.html' e passa o dicionário de contexto.
    return render(request, 'doce_gustu_app/index.html', contexto)

# View para a página de carrinho
def carrinho(request):
    """
    Renderiza a página do carrinho (carrinho.html).
    """
    return render(request, 'doce_gustu_app/carrinho.html')

# View para a página de cadastro de cliente
def cliente_cadastro_view(request):
    """
    Função da view para lidar com o cadastro de clientes.
    """
    # Se o método da requisição for POST, o formulário foi enviado.
    if request.method == 'POST':
        # Instancia o formulário com os dados da requisição.
        form = ClienteCadastroForm(request.POST)
        # Verifica se o formulário é válido.
        if form.is_valid():
            # Se o formulário for válido, salva os dados.
            # Nota: A lógica de save aqui precisará criar tanto o User quanto o Cliente.
            form.save()
            # Adiciona uma mensagem de sucesso para ser exibida ao usuário.
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
            # Redireciona para a página de login.
            return redirect('doce_gustu_app:login')
    # Se o método for GET ou o formulário for inválido, exibe o formulário vazio ou com erros.
    else:
        form = ClienteCadastroForm()

    # Renderiza o template de cadastro e passa o formulário.
    return render(request, 'doce_gustu_app/cliente_cadastro.html', {'form': form})

# View para a página do cliente logado
def cliente_logado(request):
    """
    Renderiza a página do cliente logado (cliente_logado.html).
    """
    return render(request, 'doce_gustu_app/cliente_logado.html')

# View para a página de detalhes de um produto
def produto(request):
    """
    Renderiza a página de detalhes do produto (produto.html).
    """
    return render(request, 'doce_gustu_app/produto.html')
