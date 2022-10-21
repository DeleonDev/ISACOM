from django.shortcuts import render

from apps.usuarios.models import Cliente

# Create your views here.
def finanzas(request):
    clientes = Cliente.objects.all().values('id', 'RFC')
    
    print(clientes)
    
    context = {
        'clientes': clientes
    }
    
    return render(request, 'finanzas.html', context)