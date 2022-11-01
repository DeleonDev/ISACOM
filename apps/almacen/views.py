from django.shortcuts import render

# Create your views here.
def almacen(request):
    return render(request, 'almacen.html')