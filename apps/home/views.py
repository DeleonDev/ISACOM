from django import template
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import Sum
from django.db.models.functions import ExtractMonth

from apps.ventas_compras.ventas.models import VentasDetalles


@login_required(login_url="/login/")
def index(request):
    # ? Datos para la grafica de puntos (Ventas anuales)
    # TODO: Poner en el 'filter' la obtencion de los meses en el rango del año actual
    ventas = VentasDetalles.objects.filter().annotate(
        month=ExtractMonth('fecha_factura')
    ).values('month').annotate(
        total=Sum('monto_MN')
    ).order_by('month')
    
    # TODO: Hacer las demas graficas
    ...
        
    context = {
        'segment': 'index',
        'ventas': ventas
    }

    return render(request, 'home/dashboard.html', context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
