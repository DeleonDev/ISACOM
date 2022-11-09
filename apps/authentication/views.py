# Create your views here.
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from apps.authentication.register import SetAuthGroup
from .forms import LoginForm, SignUpForm

#Inicio de sesión
def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Contraseña o usuario incorrecto'
        else:
            msg = 'Error al validar  el formulario'

    return render(request, "registration/login.html", {"form": form, "msg": msg})

# Registro de usuario
@transaction.atomic()
def register_user(request):
    if request.user.is_superuser:
        msg = None
        success = False

        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                _first_name = form.cleaned_data.get("first_name")
                _last_name = form.cleaned_data.get("last_name")
                _email = form.cleaned_data.get("email")
                _password = form.cleaned_data.get("password1")
                _rol = request.POST.get("rol", None)
                with transaction.atomic():
                    # ? Registrar usuario
                    usuario = SetAuthGroup()
                    username = usuario.username(
                        first_name=_first_name,
                        last_name=_last_name,
                    )
                    
                    user = usuario.create_user(
                        username=username,
                        password=_password,
                        first_name=_first_name,
                        last_name=_last_name,
                        email=_email
                    )
                    
                    group = usuario.create_group(name=_rol)
                    
                    usuario.user_group_add(user, group)

                    msg = f'''
                    <h4>Usuario <strong>"{username}"</strong> registrado correctamente</h4>
                    <h5>Contrasena: <strong>"{_password}"</strong></h5>
                    '''
                    success = True
            else:
                msg = 'El formulario no es válido.'
        else:
            form = SignUpForm()
        return render(request, "registration/register.html", {"form": form, "msg": msg, "success": success})
    else: return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')