from django.urls import path

from . import views

urlpatterns = [
    path('', views.finanzas, name='finanzas'),
    path('generar_pdf/', views.generar_pdf, name='generar_pdf'),
]