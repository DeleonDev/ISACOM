from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = 'Administrador'
admin.site.register(Trabajadores)
admin.site.register(Cliente)
admin.site.register(ClienteSucursal)
