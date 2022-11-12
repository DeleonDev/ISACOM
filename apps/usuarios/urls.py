from django.urls import path

from . import views

urlpatterns = [
    path('', views.usuarios, name='usuarios'),
    path('clientes/', views.clientes, name='clientes'),
    path('agregar-cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('editar-cliente/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('datos-personales/', views.datos_personales, name='datos_personales'),
    path('actualizar-datos/', views.actualizar_datos_personales, name='actualizar_datos_personales'),
    
]