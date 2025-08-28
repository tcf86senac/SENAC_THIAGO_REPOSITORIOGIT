from django.contrib import admin
# Importamos os modelos que criamos em models.py
from .models import Doce, Salgado, Bebida, Cliente

# Registramos os modelos para que eles apareçam no painel de administração do Django.
admin.site.register(Doce)
admin.site.register(Salgado)
admin.site.register(Bebida)
admin.site.register(Cliente)
