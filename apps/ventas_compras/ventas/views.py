import decimal
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.db import transaction
from apps.ventas_compras.compras.forms import ComisionesForm
from apps.ventas_compras.ventas.forms import VentasForm
from apps.ventas_compras.compras.models import Comisiones
from apps.ventas_compras.ventas.models import Ventas
from django.contrib import messages
import os
from django.db.models import Sum
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


def comisiones(request):
    comisiones = Comisiones.objects.all().order_by('fecha_inicio')
    return render(request, 'comisiones.html', {'comisiones': comisiones})


@transaction.atomic()
def comisiones_registro(request):
    if request.method == 'POST': 
        form = ComisionesForm(request.POST, instance=Comisiones())
        if form.is_valid():
            with transaction.atomic():
                instance = form.save(commit=False)
                if form.cleaned_data.get('comision') <500000:
                    instance.comision = 0
                elif form.cleaned_data.get("comision")>= 500000 and form.cleaned_data.get("comision") <= 999999:
                    instance.comision = form.cleaned_data.get("comision") * decimal.Decimal(0.05)
                elif form.cleaned_data.get("comision") >= 1000000 and form.cleaned_data.get("comision") <= 1499999:
                    instance.comision = form.cleaned_data.get("comision") * decimal.Decimal(0.07)
                elif form.cleaned_data.get("comision") >= 1500000 and form.cleaned_data.get("comision") <= 1999999:
                    instance.comision = form.cleaned_data.get("comision") * decimal.Decimal(0.09)
                elif form.cleaned_data.get("comision") >= 2000000 and form.cleaned_data.get("comision") <= 2499999:
                    instance.comision = form.cleaned_data.get("comision") * decimal.Decimal(0.11)
                elif form.cleaned_data.get("comision") >= 2500000 and form.cleaned_data.get("comision") <= 2999999:
                    instance.comision = form.cleaned_data.get("comision") * decimal.Decimal(0.13)
                instance.save()
                messages.success(request, 'Registro exitoso')
                return redirect(reverse_lazy('comisiones'))
        else:
            print(form.errors)
            messages.error(request, 'Error al registrar')
    else:
        form = ComisionesForm()
        comisiones = None
    contexto = {'form': form, 'comisiones': comisiones}
    return render(request, 'comisiones_registro.html', contexto)
