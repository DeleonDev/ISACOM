from django.urls import path
from . import views

urlpatterns = [
    path('', views.ventas, name='ventas'),
    path('registro-ventas/', views.ventas_registro, name='ventas_registro'),
    path('detalle/', views.ventas_registro_detalle, name='ventas_registro_detalle'),
    path('nuevo-registro/', views.registro, name='registro'),
]