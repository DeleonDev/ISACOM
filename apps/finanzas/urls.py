from django.urls import path

from . import views

urlpatterns = [
    path('', views.finanzas, name='finanzas')
]