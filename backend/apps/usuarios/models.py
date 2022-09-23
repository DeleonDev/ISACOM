from django.db import models
from django.contrib.auth.models import User
from apps.usuarios.options import gender_options

# Create your models here.
# * Usuarios personalizados
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    region = models.CharField(max_length=255, verbose_name='Región')
    celular = models.CharField(max_length=10, verbose_name='Celular')
    
    # Se puede poner cada uno de los cambios/funciones de 'AbstractUser'
    def __str__(self):
        return self.usuario.get_full_name()
    
    class Meta:
        db_table = "ISACOM_PERFIL"
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


# * Agente
class Agente(models.Model):
    usuario = models.OneToOneField(Perfil, on_delete=models.CASCADE, verbose_name='Usuario')
    curp = models.CharField(max_length=18, verbose_name='Curp')
    study_grade = models.CharField(max_length=100, verbose_name='Grado de estudio')
    RFC = models.CharField(max_length=13, verbose_name='RFC')
    address = models.CharField(max_length=90, verbose_name='Dirección')
    interior_num = models.CharField(max_length=10, verbose_name='Número interior')
    exterior_num = models.CharField( max_length=5, verbose_name='Número exterior')
    colony = models.CharField(max_length=50, verbose_name='Colonia')
    cp = models.CharField(max_length=5, verbose_name='C.P')
    gender = models.CharField(verbose_name='Género', choices=gender_options(), max_length=50, default=None)
    # blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE, verbose_name='Tipo de sangre')
    nss = models.CharField(max_length=11, verbose_name='No. Seguridad Social')
    # disability = models.ForeignKey(Disability, on_delete=models.CASCADE, verbose_name='Discapacidad')
    # teacher_charge = models.ForeignKey(Charge, on_delete=models.CASCADE, verbose_name='Cargo del docente')
    
    def __str__(self):
        return f'{self.usuario.usuario.get_full_name()} / {self.study_grade}'
    
    class Meta:
        db_table = "ISACOM_AGENTE"
        verbose_name = 'Agente'
        verbose_name_plural = 'Agentes'
        

# * Clientes
class Clientes(models.Model):
    usuario = models.OneToOneField(Perfil, on_delete=models.CASCADE, verbose_name='Usuario')
    identificacion = models.CharField(max_length=18, verbose_name='CURP')
    RFC = models.CharField(max_length=13, verbose_name='RFC')
    pagina_web = models.CharField(max_length=255, verbose_name='Página Web')
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, verbose_name='Agente')
    
    def __str__(self):
        return f'{self.usuario.usuario.get_full_name()} / {self.study_grade}'
    
    class Meta:
        db_table = "ISACOM_CLIENTES"
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'