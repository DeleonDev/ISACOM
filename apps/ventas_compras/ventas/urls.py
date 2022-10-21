from django.urls import path
from . import views

urlpatterns = [
    path('', views.ventas, name='ventas'),
    path('registro-ventas/', views.ventas_registro, name='ventas_registro'),
    path('nuevo-registro/', views.registro, name='registro'),
    path('detalles/', views.detalles_venta, name='detalles_venta'),
]