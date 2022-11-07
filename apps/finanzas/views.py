from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.ventas_compras.ventas.forms import VentasForm, DetallesVentasForm
from apps.ventas_compras.ventas.models import Ventas, VentasDetalles
from django.db.models import Sum

# Create your views here.


def finanzas(request):
    clientes = Cliente.objects.all().values('id', 'RFC')

    print(clientes)

    context = {
        'segment': 'finanzas',
        'ventas': ventas
    }

    return render(request, 'finanzas.html', context)


def generar_pdf(self):
    templat_route = 'apps/finanzas/templates/documentos/factura_pdf.html'
    output_path = 'static/ubicacion_pdf/factura.pdf'
    m_top, m_right, m_bottom, m_left = '10.0mm', '10.0mm', '10.0mm', '10.0mm'

    route = pdf_create(
        templat_route,
        output_path,
        m_top=m_top,
        m_right=m_right,
        m_bottom=m_bottom,
        m_left=m_left
    )

    response = HttpResponse(content_type='application/pdf')
    response[
        'Content-Disposition'] = f'attachment; filename=Factura.pdf'
    response.write(open(route, 'rb').read())
    return response
