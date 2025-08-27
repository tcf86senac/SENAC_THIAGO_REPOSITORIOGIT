# Importa o path para criar URLs
from django.urls import path
# Importa as views da sua aplicação
from . import views
# Importa as views de autenticação do Django para o login e logout
from django.contrib.auth import views as auth_views

# Define o nome da sua aplicação para o sistema de URLs
app_name = 'doce_gustu_app'

urlpatterns = [
    # Mapeia a URL raiz ('') para a view home da sua aplicação
    path('', views.home, name='home'),
    # Mapeia a URL '/carrinho/' para a view carrinho
    path('carrinho/', views.carrinho, name='carrinho'),
    # Mapeia a URL '/cadastro/' para a view cliente_cadastro
    path('cadastro/', views.cliente_cadastro, name='cliente_cadastro'),
    # Mapeia a URL '/cliente/' para a view cliente_logado
    path('cliente/', views.cliente_logado, name='cliente_logado'),
    # Mapeia a URL '/produto/' para a view produto
    path('produto/', views.produto, name='produto'),
    
    # URL para a página de login. O Django já tem uma view pronta para isso.
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # URL para a página de logout. Também é uma view pronta do Django.
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
