from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib import messages
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.models import User
from apps.usuarios.models import Trabajadores, Cliente
from .forms import ClienteForm, DatosPersonalesForm

# Create your views here.
def usuarios(request):
    usuarios = User.objects.filter(is_superuser=False).order_by('last_login')
    
    context = {'usuarios': usuarios}
    
    return render(request, 'usuarios.html', context)


def clientes(request):
    clientes = Cliente.objects.filter(agente__usuario=request.user)
    
    context = {'clientes': clientes}
    
    return render(request, 'clientes.html', context)


def agregar_cliente(request):
    user = request.user
    agente = get_object_or_404(Trabajadores, usuario=user)
    form = ClienteForm()
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=Cliente())
        if form.is_valid():
            try:
                with transaction.atomic():
                    instance = form.save(commit=False)
                    instance.agente = agente
                    instance.save()
                messages.success(request, 'Cliente agregado correctamente')
                return redirect(reverse_lazy('clientes'))
            except Exception as e:
                print(form.errors, e)
                messages.error(request, 'Error al agregar cliente')
    
    context = {'form': form}
    return render(request, 'agregar_cliente.html', context)


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(instance=cliente)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                messages.success(request, 'Cliente actualizado correctamente')
                return redirect(reverse_lazy('clientes'))
            except Exception as e:
                print(form.errors, e)
                messages.error(request, 'Error al actualizar cliente')
    
    context = {'form': form}
    return render(request, 'editar_cliente.html', context)


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