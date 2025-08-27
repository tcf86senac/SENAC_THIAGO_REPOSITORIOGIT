from django.contrib import admin
from .models import Produto, Item # Importe também o modelo Item se quiser que ele apareça

# Registra os seus modelos para que apareçam no painel de administração
admin.site.register(Produto)
admin.site.register(Item)
