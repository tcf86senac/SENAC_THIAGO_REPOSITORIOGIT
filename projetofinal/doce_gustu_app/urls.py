from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('cliente_cadastro/', views.cliente_cadastro, name='cliente_cadastro'),
    path('cliente_logado/', views.cliente_logado, name='cliente_logado'),
    path('produto/', views.produto, name='produto'),
]
