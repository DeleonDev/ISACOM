from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.db import transaction
from apps.ventas_compras.ventas.forms import  VentasForm
from apps.ventas_compras.ventas.models import Ventas
from django.contrib import messages
# Create your views here.


def ventas(request):
    ventas = Ventas.objects.all()
    return render(request, 'ventas.html', {'ventas': ventas})


@transaction.atomic
def detalles(request, id):
    form = get_object_or_404(Ventas, id=id)
    if request.method == 'POST':
        form = VentasForm(request.POST, instance=form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venta registrada con éxito')
            return redirect('ventas')
        else:
            messages.error(request, 'Ha ocurrido un error')
    else:
        form = VentasForm(instance=form)
        
    contexto = {'form': form, 'id': id}
    return render(request, 'includes/_details_ventas_modal.html', contexto)


def ventas_registro(request):
    return render(request, 'ventas_registro.html')


@transaction.atomic()
def registro(request):
    if request.method == 'POST':
        form = VentasForm(request.POST, instance=Ventas())
        if form.is_valid():
            with transaction.atomic():
                print('form is valid')
                form.save()
                messages.success(request, 'Registro exitoso')
                return redirect(reverse_lazy('ventas'))
        else:
            print('form is not valid')
            print(form.errors)
            messages.error(request, 'Error al registrar')
    else:
        print('form is not valid, reload')
        form = VentasForm()
    return render(request, 'nuevo_registro.html', {'form': form, })



def comisiones (request):
    return render(request, 'comisiones.html')
