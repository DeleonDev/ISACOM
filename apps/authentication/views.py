# Create your views here.
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import get_connection, EmailMultiAlternatives
from ISA_COM.settings import EMAIL_HOST_USER
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
                try:
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
                        <h5>Usuario <strong>"{username}"</strong> registrado correctamente</h5>
                        <h5>Se ha enviado un correo con los datos al email: <strong>"{_email}"</strong></h5>
                        '''
                        
                        content = f'''
                        <h5>Usuario <strong>"{username}"</strong></h5>
                        <h5>Contrasena: <strong>"{_password}"</strong></h5>
                        '''

                        send_user_mail( _email, content)
                        form = SignUpForm()
                except:
                    msg = 'Error al validar formulario'
            else:
                msg = 'Error al validar formulario'
        else:
            form = SignUpForm()

        return render(request, 'registration/register.html', {'form': form, 'msg': msg, 'success': success})
    else: return redirect('/')


def send_user_mail( email, content=''):
    connection = get_connection()
    connection.open()

    host_subject = 'Credenciales de acceso'

    text_content = content
                    

    message = EmailMultiAlternatives(
        host_subject,
        text_content,
        EMAIL_HOST_USER,
        [email]
    )

    message.attach_alternative(text_content, 'text/html')
    message.send()
    connection.close()
