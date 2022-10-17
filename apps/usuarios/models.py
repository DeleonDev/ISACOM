from django.db import models
from django.contrib.auth.models import User
from apps.usuarios.options import *


# ! Creacion de diccionario de estados acá

# TODO: Reestructurar el modelo de Cliente
# * Agente
class Agente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    curp = models.CharField(max_length=18, verbose_name='CURP')
    grado_estudio = models.CharField(max_length=100, verbose_name='Grado de estudio')
    rfc = models.CharField(max_length=13, verbose_name='RFC')
    direccion = models.CharField(max_length=90, verbose_name='Dirección')
    numero_interior = models.CharField(max_length=10, verbose_name='Número interior')
    numero_exterior = models.CharField( max_length=5, verbose_name='Número exterior')
    colonia = models.CharField(max_length=50, verbose_name='Colonia')
    cp = models.CharField(max_length=5, verbose_name='C.P')
    genero = models.CharField(choices=gender_options(), max_length=50, default=None, verbose_name='Género')
    
    def __str__(self):
        return self.usuario.first_name + ' ' + self.usuario.last_name
    
    class Meta:
        db_table = "ISACOM_AGENTE"
        verbose_name = 'Agente'
        verbose_name_plural = 'Agentes'
        

# * Clientes
class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    identificacion = models.CharField(max_length=18, verbose_name='CURP')
    RFC = models.CharField(max_length=13, verbose_name='RFC')
    pagina_web = models.CharField(max_length=255, verbose_name='Página Web')
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, verbose_name='Agente')
    
    def __str__(self):
        return f'{self.usuario.usuario.get_full_name()} / {self.study_grade}'
    
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
    cto_id = models.ForeignKey(Agente, on_delete=models.CASCADE, verbose_name='Contacto de la sucursal')
    def __str__(self):
        return f'{self.suc_nombre} / {self.suc_identificacion}'
    
    class Meta:
        db_table = "ISACOM_CLIENTE_SUCURSAL"
        verbose_name = 'Cliente Sucursal'
        verbose_name_plural = 'Cliente Sucursales'