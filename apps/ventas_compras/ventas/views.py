from django.shortcuts import render

# Create your views here.
def ventas(request):
    return render(request, 'ventas.html')

def ventas_registro(request):
    return render(request, 'ventas_registro.html')

def registro(request):
    return render(request, 'nuevo_registro.html')

def ventas_registro_detalle(request):
    return render(request, 'ventas/includes/_ventas_detalles.html')
