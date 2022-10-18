from django.shortcuts import redirect, render
from django.db import transaction
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render
from django.db import transaction
from apps.ventas_compras.ventas.forms import VentasForm
# Create your views here.


def ventas(request):
    return render(request, 'ventas.html')


def ventas_registro(request):
    return render(request, 'ventas_registro.html')


@transaction.atomic()
def registro(request):
    if request.method == 'POST':
        form = VentasForm(request.POST)
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
        # for field_name, field in form.fields.items():
        #     field.widget.attrs['disabled'] = False
    return render(request, 'nuevo_registro.html', {'form': form})
