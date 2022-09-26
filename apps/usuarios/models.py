from django.db import models
from django.contrib.auth.models import User
from apps.usuarios.options import gender_options, blood_type_options, disability_options

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
    tipo_sangre = models.CharField(choices=blood_type_options(), max_length=50, default=None, verbose_name='Tipo de sangre')
    nss = models.CharField(max_length=11, verbose_name='No. Seguridad Social')
    discapacidad = models.CharField(choices=disability_options(), max_length=50, default=None, verbose_name='Discapacidad')
    
    def __str__(self):
        return f'{self.usuario.get_full_name()} / {self.usuario.groups.all()[0].name}'
    
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