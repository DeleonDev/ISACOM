from distutils.command.clean import clean
from multiprocessing import context
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
    venta = VentasDetalles.objects.all()
    return render(request, 'ventas.html', {'venta': venta})

@transaction.atomic
def detalles_venta(request):
    form = get_object_or_404(Ventas)
    form2 = get_object_or_404(VentasDetalles)
    if request.method == 'POST':
        form = VentasForm(request.POST, instance=form)
        form2 = DetallesVentasForm(request.POST, instance=form2)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(request, 'Venta registrada con éxito')
            return redirect('ventas')
        else :
            messages.error(request, 'Ha ocurrido un error')
    else:
        form = VentasForm(instance=form)
        form2 = DetallesVentasForm(instance=form2)
    contexto = {'form': form, 'form2': form2}
    return render(request, 'includes/_details_ventas_modal.html', contexto)


def ventas_registro(request):
    return render(request, 'ventas_registro.html')


@transaction.atomic()
def registro(request):
    if request.method == 'POST':
        form = VentasForm(request.POST)
        form2 = DetallesVentasForm(request.POST)
        if form.is_valid() and form2.is_valid():
            with transaction.atomic():
                print('form is valid')
                form.save()
                form2.save(commit=False)
                form2.venta = form
                form2.save()
                messages.success(request, 'Registro exitoso')
                return redirect(reverse_lazy('ventas'))
        else:
            print('form is not valid')
            print(form.errors)
            print(form2.errors)
            messages.error(request, 'Error al registrar')
    else:
        print('form is not valid, reload')
        form = VentasForm()
        form2 = DetallesVentasForm()
        # for field_name, field in form.fields.items():
        #     field.widget.attrs['disabled'] = False

    return render(request, 'nuevo_registro.html', {'form': form, 'form2': form2})
