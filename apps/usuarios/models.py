from django.db import models
from django.contrib.auth.models import User, Group
from apps.usuarios.options import *

regimen = [
    ('SELECCIONE', 'SELECCIONE'),
    ('PERSONA MORAL', 'PERSONA MORAL'),
    ('PERSONA FISICA', 'PERSONA FISICA'),
]

class Trabajadores(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario', editable=False)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento', blank=True, null=True)
    rol = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Grupo', editable=False)
    genero = models.CharField(choices=gender_options(), max_length=50, default=None, verbose_name='Género')
    curp = models.CharField(max_length=18, verbose_name='CURP')
    rfc = models.CharField(max_length=13, verbose_name='RFC')
    ultimo_grado_estudio = models.CharField(max_length=100, verbose_name='Último grado de estudio')
    direccion = models.CharField(max_length=90, verbose_name='Dirección')
    numero_interior = models.CharField(max_length=3, verbose_name='Número interior')
    numero_exterior = models.CharField( max_length=3, verbose_name='Número exterior', blank=True, null=True)
    colonia = models.CharField(max_length=50, verbose_name='Colonia')
    cp = models.CharField(max_length=5, verbose_name='C.P')
    
    
    def __str__(self):
        return self.usuario.get_full_name()
        
    class Meta:
        db_table = "ISACOM_TRABAJADORES"
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'


# * Clientes
class Cliente(models.Model):
    nombre = models.CharField(max_length=250, verbose_name='Nombre')
    regimen = models.CharField(choices=regimen, max_length=50, default=None, verbose_name='Regimen')
    RFC = models.CharField(max_length=13, verbose_name='RFC')
    agente = models.ForeignKey(
        Trabajadores,
        limit_choices_to={'rol__name': 'AGENTE'},
        on_delete=models.CASCADE,
        verbose_name='Agente',
        blank=True,
        null=True,
        editable=False
    )
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "ISACOM_CLIENTE"
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        

#* Clientes sucursales

class ClienteSucursal(models.Model):
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    suc_nombre = models.CharField(max_length=75, verbose_name='Nombre de la sucursal')
    suc_identificacion = models.CharField(max_length=18, verbose_name='Indentificación de la sucursal')
    suc_direccion = models.CharField(max_length=90, verbose_name='Dirección de la sucursal')
    suc_notas = models.IntegerField(verbose_name='Notas de la sucursal')
    cto_id = models.ForeignKey(Trabajadores, limit_choices_to={'rol__name': 'AGENTE'}, on_delete=models.CASCADE, verbose_name='Contacto de la sucursal')
    def __str__(self):
        return f'{self.suc_nombre} / {self.suc_identificacion}'
    
    class Meta:
        db_table = "ISACOM_CLIENTE_SUCURSAL"
        verbose_name = 'Cliente Sucursal'
        verbose_name_plural = 'Cliente Sucursales'