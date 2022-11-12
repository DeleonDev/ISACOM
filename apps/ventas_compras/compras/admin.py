from django.contrib import admin

from apps.ventas_compras.compras.models import Comisiones, Compras

# Register your models here.

admin.site.register(Comisiones)
admin.site.register(Compras)