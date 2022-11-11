from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib import messages
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.models import User, Group
from apps.usuarios.models import Trabajadores
from .forms import DatosPersonalesForm

# Create your views here.
def usuarios(request):
    usuarios = User.objects.filter(is_superuser=False).order_by('last_login')
    
    context = {'usuarios': usuarios}
    
    return render(request, 'usuarios.html', context)


@requires_csrf_token
@transaction.atomic
def datos_personales(request):
    exist_data = False
    user = request.user
    if request.method == 'POST':
        form = DatosPersonalesForm(request.POST, instance=Trabajadores())
        if form.is_valid():
            try:
                with transaction.atomic():
                    save_personal_data(user, form)
                    messages.success(request, 'Registro exitoso')
                    return redirect(reverse_lazy('datos_personales'))
            except:
                messages.error(request, 'Error al registrar')
    else:
        if Trabajadores.objects.filter(usuario=user).exists():
            exist_data = True
            form = DatosPersonalesForm(instance=Trabajadores.objects.get(usuario=user))
        else: form = DatosPersonalesForm()
        
    context = {
        'segment': 'datos_personales',
        'exist_data': exist_data,
        'form': form
    }
    return render(request, 'datos_personales.html', context)


@requires_csrf_token
@transaction.atomic
def actualizar_datos_personales(request):
    user = request.user
    if request.method == 'POST':
        form = DatosPersonalesForm(request.POST, instance=Trabajadores.objects.get(usuario=user))
        if form.is_valid():
            try:
                with transaction.atomic():
                    save_personal_data(user, form)
                    messages.success(request, 'Registro exitoso')
                    return redirect(reverse_lazy('datos_personales'))
            except:
                messages.error(request, 'Error al registrar')
    else:
        form = DatosPersonalesForm(instance=Trabajadores.objects.get(usuario=user))
        
    context = {
        'segment': 'datos_personales',
        'form': form
    }
    return render(request, 'datos_personales.html', context)


def save_personal_data(user, form):
    instance = form.save(commit=False)
    instance.usuario = user
    instance.rol = user.groups.all()[0]
    instance.save()