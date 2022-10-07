
from django.db import models

# Create your models here.

clasif = [
    ('SELECCIONE', 'SELECCIONE'),
    ('EQUIPO', 'EQUIPO'),
    ('CONSUMIBLES', 'CONSUMIBLES'),
    ('SERVICIOS', 'SERVICIOS'),
    ('SOFTWARE', 'SOFTWARE'),
    ('OTRO', 'OTRO')
    ]

segmento = [
    ('SELECCIONE', 'SELECCIONE'),
    ('ACADEMIA', 'ACADEMIA'),
    ('INSDUSTRIA', 'INSDUSTRIA'),
    ('LAB TERCERO', 'LAB TERCERO'),
    ('ALIMENTOS', 'ALIMENTOS'),
    ('GOBIERNO', 'GOBIERNO'),
    ('DISTRIBUIDOR', 'DISTRIBUIDOR'),
    ('TERCERO', 'TERCERO'),
    ('FARMACEUTICA', 'FARMACEUTICA'),
    ('COSMETICA', 'COSMETICA'),
    ('QUIMICA', 'QUIMICA'),
    ('ELECTRONICA', 'ELECTRONICA')
    ]

estados = [
    ('SELECCIONE', 'SELECCIONE'),
    ('AGUASCALIENTES', 'AGUASCALIENTES'),
    ('BAJA CALIFORNIA', 'BAJA CALIFORNIA'),
    ('BAJA CALIFORNIA SUR', 'BAJA CALIFORNIA SUR'),
    ('CAMPECHE', 'CAMPECHE'),
    ('COAHUILA', 'COAHUILA'),
    ('COLIMA', 'COLIMA'),
    ('CHIAPAS', 'CHIAPAS'),
    ('CHIHUAHUA', 'CHIHUAHUA'),
    ('DISTRITO FEDERAL', 'DISTRITO FEDERAL'),
    ('DURANGO', 'DURANGO'),
    ('GUANAJUATO', 'GUANAJUATO'),
    ('GUERRERO', 'GUERRERO'),
    ('HIDALGO', 'HIDALGO'),
    ('JALISCO', 'JALISCO'),
    ('MEXICO', 'MEXICO'),
    ('MICHOACAN', 'MICHOACAN'),
    ('MORELOS', 'MORELOS'),
    ('NAYARIT', 'NAYARIT'),
    ('NUEVO LEON', 'NUEVO LEON'),
    ('OAXACA', 'OAXACA'),
    ('PUEBLA', 'PUEBLA'),
    ('QUERETARO', 'QUERETARO'),
    ('QUINTANA ROO', 'QUINTANA ROO'),
    ('SAN LUIS POTOSI', 'SAN LUIS POTOSI'),
    ('SINALOA', 'SINALOA'),
    ('SONORA', 'SONORA'),
    ('TABASCO', 'TABASCO'),
    ('TAMAULIPAS', 'TAMAULIPAS'),
    ('TLAXCALA', 'TLAXCALA'),
    ('VERACRUZ', 'VERACRUZ'),
    ('YUCATAN', 'YUCATAN'),
    ('ZACATECAS', 'ZACATECAS')
    ]

meses = [
    ('Enero', 'Enero'),
    ('Febrero', 'Febrero'),
    ('Marzo', 'Marzo'),
    ('Abril', 'Abril'),
    ('Mayo','Mayo'),
    ('Junio', 'Junio'),
    ('Julio', 'Julio'),
    ('Agosto', 'Agosto'),
    ('Septiembre', 'Septiembre'),
    ('Octubre', 'Octubre'),
    ('Noviembre', 'Noviembre'),
    ('Diciembre', 'Diciembre'),
]

class Clientes(models.Model):
    nombre_cliente = models.CharField(max_length=50, verbose_name='Nombre'),
    cliente_identif = models.CharField(max_length=50, verbose_name='Identificacion cliente'),
    cliente_rfc = models.CharField(max_length=13, verbose_name='RFC cliente'),
    
    