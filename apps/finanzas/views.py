import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from apps.ventas_compras.ventas.forms import DetallesVentasForm
from apps.ventas_compras.ventas.models import Ventas, VentasDetalles
from django.db import transaction
from django.db.models import Sum
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import requires_csrf_token


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
        .order_by('incentivo')
    
    saldo_restante = venta_detalles.filter(venta_id=orden_compra_id) \
        .aggregate(total=venta.cotizacion-Sum('importe_USD'))['total']
        
    if request.method == 'POST':
        form = DetallesVentasForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.venta_id = orden_compra_id
            instance.fecha_pago = datetime.date.today()
            instance.save()
            messages.success(request, 'Pago registrado con éxito')
            return redirect('agregar_pago_factura', orden_compra_id)
        else:
            print(form.errors)
            messages.error(request, 'Ha ocurrido un error al registrar el pago')
            # return redirect('agregar_pago_factura', orden_compra_id)
    
    context = {
        'segment': 'finanzas',
        'venta': venta,
        'form': form,
        'historial_pagos': historial_pagos,
        'saldo_restante': saldo_restante
    }
    
    return render(request, 'agregar_pago_factura.html', context)

@transaction.atomic
@requires_csrf_token
def cargar_factura(request, id):
    venta_detalle = get_object_or_404(VentasDetalles, id=id)
    if request.method == 'POST' and request.FILES['factura']:
        try:
            with transaction.atomic():
                myfile = request.FILES['factura']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                # update or create
                VentasDetalles.objects.update_or_create(
                    id=id,
                    defaults={
                        'factura': uploaded_file_url,
                        'fecha_factura': datetime.date.today()
                    }
                )
                messages.success(request, 'Factura cargada con éxito')
        except: messages.error(request, 'Ha ocurrido un error al cargar la factura')
        return redirect('agregar_pago_factura', venta_detalle.venta_id)
    return render(request, 'includes/factura_modal.html', {'id': id})



def ventas_detalles(request, id):
    ventas_detalles = get_object_or_404(VentasDetalles, id=id)
    print(ventas_detalles.id)
    if request.method == 'POST':
        form = DetallesVentasForm(request.POST, instance=ventas_detalles)
        if form.is_valid():
            with transaction.atomic():
                instance = form.save(commit=False)
                instance.venta_id = ventas_detalles.venta_id
                instance.save()
                messages.success(request, 'Registro exitoso')
                return redirect('ventas_detalles', id)
        else:
            print(form.errors)
            messages.error(request, 'Error al registrar')
    else:
        form = DetallesVentasForm(instance=ventas_detalles)
        print(form)
        
    context = {
        'id': id,
        'form': form,
    }
    return render(request, 'detalles_finanza.html', context)