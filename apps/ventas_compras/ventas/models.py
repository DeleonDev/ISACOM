from django.db import models
from apps.usuarios.models import Trabajadores, Cliente

from apps.ventas_compras.ventas.options import segment_options
from apps.usuarios.options import *

# Create your models here.
states = [
    ('SELECCIONE', 'SELECCIONE'),
    ('AGUASCALIENTES', 'AGUASCALIENTES'),
    ('BAJA CALIFORNIA', 'BAJA CALIFORNIA'),
    ('BAJA CALIFORNIA SUR', 'BAJA CALIFORNIA SUR'),
    ('CAMPECHE', 'CAMPECHE'),
    ('COAHUILA', 'COAHUILA'),
    ('COLIMA', 'COLIMA'),
    ('CHIAPAS', 'CHIAPAS'),
    ('CHIHUAHUA', 'CHIHUAHUA'),
    ('CIUDAD DE MÉXICO', 'CIUDAD DE MÉXICO'),
    ('DURANGO', 'DURANGO'),
    ('GUANAJUATO', 'GUANAJUATO'),
    ('GUERRERO', 'GUERRERO'),
    ('HIDALGO', 'HIDALGO'),
    ('JALISCO', 'JALISCO'),
    ('MÉXICO', 'MÉXICO'),
    ('MICHOACÁN', 'MICHOACÁN'),
    ('MORELOS', 'MORELOS'),
    ('NAYARIT', 'NAYARIT'),
    ('NUEVO LEÓN', 'NUEVO LEÓN'),
    ('OAXACA', 'OAXACA'),
    ('PUEBLA', 'PUEBLA'),
    ('QUERÉTARO', 'QUERÉTARO'),
    ('QUINTANA ROO', 'QUINTANA ROO'),
    ('SAN LUIS POTOSÍ', 'SAN LUIS POTOSÍ'),
    ('SINALOA', 'SINALOA'),
    ('SONORA', 'SONORA'),
    ('TABASCO', 'TABASCO'),
    ('TAMAULIPAS', 'TAMAULIPAS'),
    ('TLAXCALA', 'TLAXCALA'),
    ('VERACRUZ', 'VERACRUZ'),
    ('YUCATÁN', 'YUCATÁN'),
    ('ZACATECAS', 'ZACATECAS'),
    ('EXTRANJERO', 'EXTRANJERO'),
    ('NO APLICA', 'NO APLICA'),
    ('OTRO', 'OTRO'),
]

class Ventas(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente', serialize=False)
    segmento = models.CharField(choices=segment_options(), max_length=50, default=None, verbose_name='segmento')
    estado = models.CharField(max_length=50, verbose_name='Estado', default=None, choices=states)
    agente = models.ForeignKey(Trabajadores, limit_choices_to={'rol__name': 'AGENTE'}, on_delete=models.CASCADE, verbose_name='Agente')
    cotizacion = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cotización')
    descripcion = models.TextField(verbose_name='Descripción')
    clasificacion = models.CharField(choices=clasification_options(), max_length=50, default=None, verbose_name='Clasificación')
    orden_compra = models.CharField(max_length=50, verbose_name='Orden de compra')
    fecha_orden_compra = models.DateField(verbose_name='Fecha de orden de compra')
    
    def __str__(self):
        return f'{self.cliente} - {self.orden_compra} ({self.cotizacion})'
    
    class Meta:
        db_table = "ISACOM_VENTAS"
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
    
class VentasDetalles(models.Model):
    comision = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Comisión', editable=False, default=0)
    concepto = models.CharField(max_length=50, verbose_name='Concepto')
    fecha_pago = models.DateField(verbose_name='Fecha de pago', editable=False, null=True)
    factura = models.FileField(verbose_name='Factura', editable=False, null=True)
    fecha_factura = models.DateField(verbose_name='Fecha de factura', editable=False, blank=True, null=True)
    monto_USD = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Monto en USD')
    monto_MN = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Monto en MN')
    incentivo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Incentivo')
    tipo_cambio_factura = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Tipo de cambio de factura')
    tipo_cambio_oc = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Tipo de cambio de orden de compra')
    importe_USD = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Importe en USD')
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE, verbose_name='Venta', editable=False)
    
    def __str__(self):
        return f'{self.venta} - {self.factura}'
    
    class Meta:
        db_table = "ISACOM_VENTAS_DETALLES"
        verbose_name = 'Venta detalle'
        verbose_name_plural = 'Ventas detalles'
    