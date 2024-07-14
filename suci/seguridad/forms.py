from django import forms
from django.forms import ModelForm
from .models import *
from seguridad.models import Entradap, Salidap, Gestion, Vehiculos

# FORMULARIO DE ENTRADA PERSONAL
class EntradapForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    hora = forms.CharField(widget=forms.TextInput(attrs={'type':'time'}))
    class Meta:
        model = Entradap
        fields = ('name', 'apellido', 'cedula', 'telefono', 'fecha', 'direccion', 'cargo', 'hora')

# FORMULARIO DE ACTUALIZACIÓN ENTRADA PERSONAL
class EntradapEForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    hora = forms.CharField(widget=forms.TextInput(attrs={'type':'time'}))
    class Meta:
        model = Entradap
        fields = ('name', 'apellido', 'cedula', 'telefono', 'fecha', 'direccion', 'cargo', 'hora')

# FORMULARIO DE SALIDA PERSONAL
class SalidapForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    hora = forms.CharField(widget=forms.TextInput(attrs={'type':'time'}))
    class Meta:
        model = Salidap
        fields = ('name', 'apellido', 'cedula', 'telefono', 'fecha', 'direccion', 'cargo', 'hora')

# FORMULARIO DE ACTUALIZACIÓN SALIDA PERSONAL
class SalidapEForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    hora = forms.CharField(widget=forms.TextInput(attrs={'type':'time'}))
    class Meta:
        model = Salidap
        fields = ('name', 'apellido', 'cedula', 'telefono', 'fecha', 'direccion', 'cargo', 'hora')

# FORMULARIO DE GESTIÓN DE INCIDENTES
class GestionForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    hora = forms.CharField(widget=forms.TextInput(attrs={'type':'time'}))
    class Meta:
        model = Gestion
        fields = ('name', 'apellido', 'cedula',  'tipo', 'descripcion', 'fecha', 'direccion', 'cargo', 'hora')

# FORMULARIO DE ACTUALIZACIÓN GESTIÓN DE INCIDENTES
class GestionEForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    hora = forms.CharField(widget=forms.TextInput(attrs={'type':'time'}))
    class Meta:
        model = Gestion
        fields = ('name', 'apellido', 'cedula', 'tipo', 'descripcion', 'fecha', 'direccion', 'cargo', 'hora')

# FORMULARIO DE VEHICULOS
class VehiculosForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    hora = forms.CharField(widget=forms.TextInput(attrs={'type':'time'}))
    class Meta:
        model = Vehiculos
        fields = ('nombre', 'apellido', 'cedula', 'modelo', 'vehiculo', 'motivo', 'capagasolina', 'cantigasolina', 'placa', 'fecha', 'hora')

# FORMULARIO DE ACTUALIZACIÓN VEHICULOS
class VehiculosEForm(forms.ModelForm):
    fecha = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    hora = forms.CharField(widget=forms.TextInput(attrs={'type':'time'}))
    class Meta:
        model = Vehiculos
        fields = ('nombre', 'apellido', 'cedula', 'modelo', 'vehiculo', 'motivo', 'capagasolina', 'cantigasolina', 'placa', 'fecha', 'hora')