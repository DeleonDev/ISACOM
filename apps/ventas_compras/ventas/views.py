from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.db import transaction
from apps.ventas_compras.ventas.forms import DetallesVentasForm, VentasForm
from apps.ventas_compras.ventas.models import Ventas, VentasDetalles
from django.contrib import messages
# Create your views here.


def ventas(request):
    ventas = Ventas.objects.all().order_by('fecha_orden_compra')
    return render(request, 'ventas.html', {'ventas': ventas})


def detalles(request, id):
    form = get_object_or_404(Ventas, id=id)
    if request.method == 'POST':
        form = VentasForm(request.POST, instance=form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venta actualizada con éxito')
            return redirect('ventas')
        else:
            print(form.errors)
            messages.error(request, 'Ha ocurrido un error')
    else:
        form = VentasForm(instance=form)
    contexto = {'form': form, 'id': id}
    return render(request, 'detalles_venta.html', contexto)


def ventas_registro(request):
    return render(request, 'ventas_registro.html')


@transaction.atomic()
def registro(request):
    if request.method == 'POST':
        form = VentasForm(request.POST, instance=Ventas())
        if form.is_valid():
            with transaction.atomic():
                form.save()
                messages.success(request, 'Registro exitoso')
                return redirect(reverse_lazy('ventas'))
        else:
            print(form.errors)
            messages.error(request, 'Error al registrar')
    else:
        form = VentasForm()
    return render(request, 'nuevo_registro.html', {'form': form})


def comisiones (request):
    return render(request, 'comisiones.html')
