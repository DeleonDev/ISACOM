from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from apps.ventas_compras.compras.forms import ComprasForm
from django.db import transaction
from apps.ventas_compras.compras.models import Compras
from django.contrib import messages

# Create your views here.
def compras(request):
    compras = Compras.objects.filter(fecha_entrega__isnull=True).order_by('fecha_entrega_estimada')
    compras_completadas = Compras.objects.filter(fecha_entrega__isnull=False).order_by('fecha_entrega')
    return render(request, 'compras.html', {'compras': compras, 'compras_completadas': compras_completadas})

@transaction.atomic()
def agregar_compra(request):
    if request.method == 'POST':
        form = ComprasForm(request.POST, instance=Compras())
        if form.is_valid():
            with transaction.atomic():
                form.save()
                messages.success(request, 'Registro exitoso')
                return redirect(reverse_lazy('compras'))
        else:
            print(form.errors)
            messages.error(request, 'Error al registrar')
            
    else:
        form = ComprasForm()
    return render(request, 'agregar_compra.html', {'form': form})

def compras_detalle(request, id):
    form = get_object_or_404(Compras, id=id)
    if request.method == 'POST':
        form = ComprasForm(request.POST, instance=form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compra actualizada con éxito')
            return redirect('compras')
        else:
            print(form.errors)
            messages.error(request, 'Ha ocurrido un error')
    else:
        form = ComprasForm(instance=form)
    contexto = {'form': form, 'id': id}
    return render(request, 'compras_detalle.html', contexto)