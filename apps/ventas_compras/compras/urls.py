from django.urls import path
from . import views

urlpatterns = [
    path('', views.compras, name='compras'),
    path('registro_compra/', views.agregar_compra, name='agregar_compra'),
    path ('compras_detalle/<int:id>', views.compras_detalle, name='compras_detalle'),
]