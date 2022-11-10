from django.urls import path

from . import views

urlpatterns = [
    path('', views.usuarios, name='usuarios'),
    path('datos-personales/', views.datos_personales, name='datos_personales'),
    path('actualizar-datos/', views.actualizar_datos_personales, name='actualizar_datos_personales'),
    
]