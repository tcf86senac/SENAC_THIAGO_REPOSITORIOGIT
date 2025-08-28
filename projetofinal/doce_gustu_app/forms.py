# doce_gustu_app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente

# Cria um formulário personalizado para o cadastro de clientes.
# Ele herda de UserCreationForm, que já lida com o nome de usuário e senha.
class ClienteCadastroForm(UserCreationForm):
    # Campos adicionais do modelo Cliente.
    # Usamos CharField para campos de texto.
    nome = forms.CharField(max_length=100, label="Nome")
    sobrenome = forms.CharField(max_length=100, label="Sobrenome")
    telefone = forms.CharField(max_length=20, label="Telefone")
    endereco_entrega = forms.CharField(max_length=255, label="Endereço de Entrega")
    ponto_referencia = forms.CharField(max_length=255, required=False, label="Ponto de Referência")
    observacoes = forms.CharField(widget=forms.Textarea, required=False, label="Observações")

    # A classe Meta conecta o formulário a um modelo específico, mas como
    # estamos combinando dados de dois modelos, faremos a criação do usuário
    # e do cliente na view.

