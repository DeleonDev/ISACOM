
from django.db import models

from apps.usuarios.models import Trabajadores
from apps.ventas_compras.ventas.models import Ventas, VentasDetalles

# Create your models here.

class Comisiones(models.Model):
    trabajadores = models.ForeignKey(Trabajadores, on_delete=models.CASCADE, verbose_name='Trabajador')
    comision = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Venta total', null=True, blank=True)
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
    fecha_fin = models.DateField(verbose_name='Fecha de fin')
    
    def __str__(self):
        return f'{self.comision}'
    
    class Meta:
        db_table = "ISACOM_COMISIONES"
        verbose_name = 'Comisión'
        verbose_name_plural = 'Comisiones'
        
        
class Compras(models.Model):
    orden_compra = models.ForeignKey(VentasDetalles, on_delete=models.CASCADE, verbose_name='Orden de compra')
    fecha_entrega_estimada = models.DateField(verbose_name='Fecha estimada de entrega')    
    fecha_entrega = models.DateField(verbose_name='Fecha real de entrega', null=True, blank=True)
    documento_compra = models.FileField(verbose_name='Factura', null=True, blank=True)
    def __str__(self):
        return f'{self.orden_compra}'
    
    class Meta:
        db_table = "ISACOM_COMPRAS"
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'