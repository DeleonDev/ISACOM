from django import template
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import Sum
from django.db.models.functions import ExtractMonth
import datetime

from apps.ventas_compras.ventas.models import VentasDetalles


@login_required(login_url="/login/")
def index(request):
    primer_dia = datetime.date(datetime.date.today().year, 1, 1)
    ultimo_dia = datetime.date(datetime.date.today().year, 12, 31)
    
    # ? Datos para la grafica de puntos (Ventas anuales)
    ventas_anuales = VentasDetalles.objects \
        .filter(fecha_factura__range=(primer_dia, ultimo_dia)) \
        .annotate(mes=ExtractMonth('fecha_factura')) \
        .values('mes') \
        .annotate(total=Sum('monto_MN')) \
        .order_by('mes')
    

        
    context = {
        'segment': 'index',
        'ventas_anuales': ventas_anuales
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
