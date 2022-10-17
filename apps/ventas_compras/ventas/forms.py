from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from django.utils.translation import gettext_lazy as _
from django import forms
import re
from datetime import date
from apps.usuarios.models import Agente, Cliente

from apps.ventas_compras.ventas.models import Ventas


class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'fecha_orden_compra': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def clean_cliente(self):
        cliente =self.cleaned_data['cliente']
        if cliente == 'SELECCIONE':
            raise ValidationError(
                _('Seleccione un cliente'),
            )
        return cliente
    
    def clean_segmento(self):
        segmento = self.cleaned_data['segmento']
        if segmento == 'SELECCIONE':
            raise ValidationError(
                _('Seleccione un segmento'),
            )
        return segmento
    
    def clean_states(self):
        states = self.cleaned_data['states']
        if states == 'SELECCIONE':
            raise ValidationError(
                _('Seleccione un estado'),
            )
        return states
    
    def clean_agente(self):
        agente =self.cleaned_data['agente']
        if agente == 'SELECCIONE':
            raise ValidationError(
                _('Seleccione un agente'),
            )
        return agente

    def clean_cotizacion(self):
        cotizacion = self.cleaned_data['cotizacion']
        if not re.match(r'^[0-9]+$', cotizacion):
            raise ValidationError(
                _('Ingrese un número de cotización válido'),
            )
            
        return cotizacion
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        if not re.match(r'^[a-zA-Z0-9]+$', descripcion):
            raise ValidationError(
                _('Ingrese una descripción válida'),
            )
            
        return descripcion
    
    def clean_clasificacion(self):
        clasificacion = self.cleaned_data['clasificacion']
        if clasificacion == 'SELECCIONE':
            raise ValidationError(
                _('Seleccione una clasificación'),
            )
        return clasificacion
    
    def clean_orden_compra(self):
        orden_compra = self.cleaned_data['orden_compra']
        if not re.match(r'^[0-9]+$', orden_compra):
            raise ValidationError(
                _('Ingrese un número de orden de compra válido'),
            )
            
        return orden_compra
    
    def clean_fecha_orden_compra(self):
        fecha_orden_compra = self.cleaned_data['fecha_orden_compra']
        if fecha_orden_compra > date.today():
            raise ValidationError(
                _('Ingrese una fecha de orden de compra válida'),
            )
            
        return fecha_orden_compra
    
    def __init__(self, *args, **kwargs):
        super(VentasForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].empty_label = 'SELECCIONE'
        for field_name, field in self.fields.items():
            field.widget.attrs['onkeyup'] = 'javascript:this.value=this.value.toUpperCase()'
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  
            if field_name in ['company_email']:
                field.widget.attrs['onkeyup'] = ''