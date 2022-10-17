from audioop import reverse
from django.shortcuts import redirect, render
from django.db import transaction
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render
from django.db import transaction
from apps.usuarios.models import Cliente
from apps.ventas_compras.ventas.forms import VentasForm
# Create your views here.


def ventas(request):
    return render(request, 'ventas.html')


def ventas_registro(request):
    return render(request, 'ventas_registro.html')


@transaction.atomic()
def registro(request):
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        formulario_ventas = VentasForm(request.POST)
        with transaction.atomic():
            formulario_ventas.save(commit=False)
            formulario_ventas.cliente = request.POST.get('cliente', ' ')
            formulario_ventas.save()
            messages.success(request, 'Registro exitoso')
            
    else:
        form = VentasForm()
        for field_name, field in form.fields.items():
            field.widget.attrs['disabled'] = False
    return render(request, 'nuevo_registro.html', {'formulario_uno': form}, {'clientes': clientes})



