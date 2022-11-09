from django.urls import path

from . import views

urlpatterns = [
    path('', views.finanzas, name='finanzas'),
    path('agregar-pago-factura/<int:orden_compra_id>', views.agregar_pago_factura, name='agregar_pago_factura'),
    path('generar_pdf/', views.generar_pdf, name='generar_pdf'),
    path('cargar-factura/<int:id>', views.cargar_factura, name='cargar_factura'),
]