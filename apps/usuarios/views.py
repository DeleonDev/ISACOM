from urllib import response
from django.shortcuts import render
from apps.usuarios.models import Agente, User
# Create your views here.
def usuarios(request):
    usuarios = Agente.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})


