from django import template
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import Sum, Count
from django.db.models.functions import ExtractMonth
import datetime

from apps.ventas_compras.ventas.models import VentasDetalles


@login_required(login_url="/login/")
def index(request):
    primer_dia = datetime.date(datetime.date.today().year, 1, 1)
    ultimo_dia = datetime.date(datetime.date.today().year, 12, 31)
    
    detalle_ventas = VentasDetalles.objects.filter(
        venta__fecha_orden_compra__range=(primer_dia, ultimo_dia)
    )
    
    # ? Ventas anuales
    ventas_anuales = detalle_ventas \
        .annotate(mes=ExtractMonth('venta__fecha_orden_compra')) \
        .values('mes') \
        .annotate(total=Sum('monto_USD')) \
        .order_by('mes')
        
    # ? Ventas por clasificacion
    ventas_clasificacion = detalle_ventas \
        .values('venta__clasificacion') \
        .annotate(total=Sum('monto_USD'), cantidad=Count('venta__clasificacion')) \
    
    total_ventas_clasificacion = detalle_ventas.aggregate(total=Sum('monto_USD'), cantidad=Count('venta__clasificacion'))

    # ? Ventas por segmento
    ventas_segmento = detalle_ventas \
        .values('venta__segmento') \
        .annotate(total=Sum('monto_USD'), cantidad=Count('venta__segmento'))
        
    # ? Ventas por vendedor
    ventas_vendedor = detalle_ventas \
        .values('venta__agente') \
        .annotate(
            total=Sum('monto_USD'),
            cantidad=Count('venta'),
            promedio=Sum('monto_USD') / Count('venta')
        )
        
    context = {
        'segment': 'index',
        'ventas_anuales': ventas_anuales,
        'ventas_clasificacion': ventas_clasificacion,
        'total_ventas_clasificacion': total_ventas_clasificacion,
        'ventas_segmento': ventas_segmento,
        'ventas_vendedor': ventas_vendedor
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
