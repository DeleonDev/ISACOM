from django.urls import path

from . import views

urlpatterns = [
    path('', views.finanzas, name='finanzas'),
    path('agregar-pago-factura/<int:orden_compra_id>', views.agregar_pago_factura, name='agregar_pago_factura'),
    path('generar-pdf/<str:factura>', views.generar_pdf, name='generar_pdf'),
]