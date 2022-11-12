from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re
from datetime import date

from apps.ventas_compras.compras.models import Comisiones, Compras


class ComisionesForm(forms.ModelForm):
    class Meta:
        model = Comisiones
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
    
    def clean_comision(self):
        comision = self.cleaned_data['comision']
        return comision
    
    def clean_fecha_inicio(self):
        fecha_inicio = self.cleaned_data['fecha_inicio']
        if fecha_inicio > date.today():
            raise ValidationError(
                _('La fecha de inicio no puede ser mayor a la fecha actual'),
            )
        return fecha_inicio
    
    def clean_fecha_fin(self):
        fecha_fin = self.cleaned_data['fecha_fin']
        if fecha_fin > date.today():
            raise ValidationError(
                _('La fecha de fin no puede ser mayor a la fecha actual'),
            )
        return fecha_fin
    
    def clean_trabajadores(self):
        trabajadores = self.cleaned_data['trabajadores']
        if trabajadores == 'SELECCIONE':
            raise ValidationError(
                _('Seleccione un vendedor'),
            )
        return trabajadores
    
    
    def __init__(self, *args, **kwargs):
        super(ComisionesForm, self).__init__(*args, **kwargs)
        self.fields['trabajadores'].empty_label = 'SELECCIONE'
        for field_name, field in self.fields.items():
            field.widget.attrs['onkeyup'] = 'javascript:this.value=this.value.toUpperCase()'
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
            field.widget.attrs['autocomplete'] = 'off'
            field.widget.attrs['accept'] = ''
        if field_name in ['fecha_inicio', 'fecha_fin']:
                field.widget.attrs['onkeyup'] = ''
                
                
class ComprasForm(forms.ModelForm):
    class Meta:
        model = Compras
        fields = '__all__'
        widgets = {
            'fecha_entrega_estimada': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
        
    def clean_orden_compra(self):
        orden_compra = self.cleaned_data['orden_compra']
        return orden_compra
    
    
    def clean_fecha_entrega_estimada(self):
        fecha_entrega_estimada = self.cleaned_data['fecha_entrega_estimada']
        return fecha_entrega_estimada
    
    def clean_fecha_entrega(self):
        fecha_entrega = self.cleaned_data['fecha_entrega']
        return fecha_entrega
    
    def __init__(self, *args, **kwargs):
        super(ComprasForm, self).__init__(*args, **kwargs)
        self.fields['orden_compra'].empty_label = 'SELECCIONE'
        for field_name, field in self.fields.items():
            field.widget.attrs['onkeyup'] = 'javascript:this.value=this.value.toUpperCase()'
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
            field.widget.attrs['autocomplete'] = 'off'
            field.widget.attrs['accept'] = ''
        if field_name in ['fecha_entrega_estimada', 'fecha_entrega']:
                field.widget.attrs['onkeyup'] = ''