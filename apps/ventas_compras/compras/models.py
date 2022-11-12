
from django.db import models

from apps.usuarios.models import Trabajadores

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