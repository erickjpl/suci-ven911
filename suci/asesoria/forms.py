from django import forms
from django.forms import ModelForm
from .models import *
from .models import Denuncia, RegistroFilmico

class FormDenuncia(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = [
            'estatus',
            'ente',
            'nombres_d',
            'apellidos_d',
            'cedula_d',
            'telefono',
            'email',
            'direccion_d',
            'nombres_denunciado',
            'apellidos_denunciado',
            'cedula_denunciado',
            'motivo',
            'zona',
            'fecha_denuncia',
            'fecha_incidente',
        ]
        
class FormRegistroF(forms.ModelForm):
    class Meta:
        model = RegistroFilmico
        fields = [
            'estatus',
            'direccion',
            'camara',
            'motivo_solicitud',
            'ente_solicita',
            'fecha_solicitud',
            'fecha_culminacion',
        ]