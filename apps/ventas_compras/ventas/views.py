from django.shortcuts import get_object_or_404, redirect, render
from django.db import transaction
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render
from django.db import transaction
from apps.ventas_compras.ventas.forms import DetallesVentasForm, VentasForm
from apps.ventas_compras.ventas.models import Ventas, VentasDetalles
# Create your views here.


def ventas(request):
    venta = VentasDetalles.objects.all()
    return render(request, 'ventas.html', {'venta': venta})

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
