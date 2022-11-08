from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.finanzas.generar_pdf import pdf_create
from apps.ventas_compras.ventas.forms import VentasForm, DetallesVentasForm
from apps.ventas_compras.ventas.models import Ventas, VentasDetalles
from django.db.models import Sum

# Create your views here.


def finanzas(request):
    ventas = Ventas.objects.all()
    
    context = {
        'segment': 'finanzas',
        'ventas': ventas
    }
    
    return render(request, 'finanzas.html', context)


def agregar_pago_factura(request, orden_compra_id):
    venta = get_object_or_404(Ventas, id=orden_compra_id)
    form = DetallesVentasForm()
    venta_detalles = VentasDetalles.objects
    
    historial_pagos = venta_detalles.filter(venta_id=orden_compra_id) \
        .order_by('comision')
    
    saldo_restante = venta_detalles.filter(venta_id=orden_compra_id) \
        .aggregate(total=venta.cotizacion-Sum('importe_USD'))['total']
        
    if request.method == 'POST':
        form = DetallesVentasForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.venta_id = orden_compra_id
            instance.save()
            messages.success(request, 'Pago registrado con éxito')
            return redirect('agregar_pago_factura', orden_compra_id)
        else:
            messages.error(request, 'Ha ocurrido un error al registrar el pago')
            return redirect('agregar_pago_factura', orden_compra_id)
    
    context = {
        'segment': 'finanzas',
        'venta': venta,
        'form': form,
        'historial_pagos': historial_pagos,
        'saldo_restante': saldo_restante
    }
    
    return render(request, 'agregar_pago_factura.html', context)

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


def cargar_factura(request,id):
    
    return render(request, 'finanzas/includes/factura_modal.html', {'id':id})
