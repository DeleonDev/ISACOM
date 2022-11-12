from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re
from .models import Trabajadores, Cliente

class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = Trabajadores
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
    
    def clean_genero(self):
        genero = self.cleaned_data['genero']
        if genero == 'SELECCIONE':
            raise ValidationError(
                _('Seleccione un género'),
            )
        return genero

    def clean_curp(self):
        curp = self.cleaned_data['curp']
        if not re.match(r'^[A-Z]{4}[0-9]{6}[H,M][A-Z]{5}[A-Z,0-9]{2}$', curp):
            raise ValidationError(
                _('Ingrese una CURP válida'),
            )
        return curp

    def clean_rfc(self):
        rfc = self.cleaned_data['rfc']
        if not re.match(r'^[A-Z]{4}[0-9]{6}[A-Z,0-9]{3}$', rfc):
            raise ValidationError(
                _('Ingrese un RFC válido'),
            )
        return rfc
    
    def clean_ultimo_grado_estudios(self):
        return self.cleaned_data['ultimo_grado_estudios']
    
    def clean_direreccion(self):
        return self.cleaned_data['direccion']
    
    def clean_numero_interior(self):
        numero_interior = self.cleaned_data['numero_interior']
        if not re.match(r'^[0-9]+$', numero_interior):
            raise ValidationError(
                _('Ingrese un número de interior válido'),
            )
        return numero_interior
    
    def clean_numero_exterior(self):
        numero_exterior = self.cleaned_data['numero_exterior']
        if not re.match(r'^[0-9]+$', numero_exterior):
            raise ValidationError(
                _('Ingrese un número de exterior válido'),
            )
        return numero_exterior
    
    def clean_colonia(self):
        return self.cleaned_data['colonia']
    
    def clean_cp(self):
        cp = self.cleaned_data['cp']
        if not re.match(r'^[0-9]{5}$', cp):
            raise ValidationError(
                _('Ingrese un código postal válido'),
            )
        return cp
    
    def __init__(self, *args, **kwargs):
        super(DatosPersonalesForm, self).__init__(*args, **kwargs)
        self.fields['genero'].empty_label = 'SELECCIONE'
        for field_name, field in self.fields.items():
            field.widget.attrs['onkeyup'] = 'javascript:this.value=this.value.toUpperCase()'
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['autocomplete'] = 'off'
            field.widget.attrs['placeholder'] = field.label
        if field_name in ['fecha_nacimiento']:
            field.widget.attrs['onkeyup'] = ''
        if field_name in ['numero_exterior']:
            field.widget.attrs['required'] = ''


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def clean_nombre(self):
        return self.cleaned_data['nombre']
    
    def clean_regimen(self):
        regimen = self.cleaned_data['regimen']
        if regimen == 'SELECCIONE':
            raise ValidationError(
                _('Seleccione un régimen'),
            )
        return regimen

    def clean_rfc(self):
        rfc = self.cleaned_data['rfc']
        if not re.match(r'^[A-Z]{4}[0-9]{6}[A-Z,0-9]{3}$', rfc):
            raise ValidationError(
                _('Ingrese un RFC válido'),
            )
        return rfc
    
    
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['regimen'].empty_label = 'SELECCIONE'
        for field_name, field in self.fields.items():
            field.widget.attrs['onkeyup'] = 'javascript:this.value=this.value.toUpperCase()'
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['autocomplete'] = 'off'
            field.widget.attrs['placeholder'] = field.label