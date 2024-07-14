from django import forms
from django.forms import ModelForm
from .models import *
from administracion.models import Bienes, Consumible, Mobiliario, Averia, Compras, Asignacion

#FORMULARIO DE BIENES
class BienesForm(forms.ModelForm):
    fecha_adq = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Bienes
        fields = ('descripcion', 'marca', 'modelo', 'serial', 'cantidad', 'asignado', 'valor', 'condicion', 'ubicacion', 'garantia', 'fecha_adq')

#FORMULARIO DE BIENES - ACTUALIZADO
class BienesEForm(forms.ModelForm):
    fecha_adq = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Bienes
        fields = ('descripcion', 'marca', 'modelo', 'serial', 'cantidad', 'asignado', 'valor', 'condicion', 'ubicacion', 'garantia', 'fecha_adq')

#FORMULARIO DE CONSUMIBLE
class ConsumibleForm(forms.ModelForm):
    fecha_adq = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Consumible
        fields = ('descripcion', 'marca', 'serial', 'cantidad', 'valor', 'condicion', 'ubicacion', 'observaciones', 'fecha_adq')

#FORMULARIO DE CONSUMIBLE - ACTUALIZADO
class ConsumibleEForm(forms.ModelForm):
    fecha_adq = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Consumible
        fields = ('descripcion', 'marca', 'serial', 'cantidad', 'valor', 'condicion', 'ubicacion', 'observaciones', 'fecha_adq')

#FORMULARIO DE MOBILIARIO
class MobiliarioForm(forms.ModelForm):
    fecha_adq = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Mobiliario
        fields = ('descripcion', 'marca', 'serial', 'cantidad', 'valor', 'condicion', 'ubicacion', 'observaciones', 'codigo_bn', 'fecha_adq')

#FORMULARIO DE MOBILIARIO - ACTUALIZADO
class MobiliarioEForm(forms.ModelForm):
    fecha_adq = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Mobiliario
        fields = ('descripcion', 'marca', 'serial', 'cantidad', 'valor', 'condicion', 'ubicacion', 'observaciones', 'codigo_bn', 'fecha_adq')

#FORMULARIO DE AVERIA
class AveriaForm(forms.ModelForm):
    fecha_adq = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Averia
        fields = ('bienes', 'sintomas', 'departamento_ave', 'problema', 'condicion', 'ubicacion', 'codigo_bn', 'fecha_adq')

#FORMULARIO DE AVERIA - ACTUALIZADO
class AveriaEForm(forms.ModelForm):
    fecha_adq = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Averia
        fields = ('bienes', 'sintomas', 'departamento_ave', 'problema', 'condicion', 'ubicacion', 'codigo_bn', 'fecha_adq')


#FORMULARIO DE COMPRAS
class ComprasForm(forms.ModelForm):
    fecha_adq = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Compras
        fields = ('producto', 'serial', 'marca', 'modelo', 'numero_orden', 'valor', 'cantidad', 'proveedor', 'ubicacion', 'garantia', 'fecha_adq')

#FORMULARIO DE COMPRAS
class ComprasEForm(forms.ModelForm):
    fecha_adq = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Compras
        fields = ('producto', 'serial', 'marca', 'modelo', 'numero_orden', 'valor', 'cantidad', 'proveedor', 'ubicacion', 'garantia', 'fecha_adq')

#FORMULARIO DE ASIGNADO
class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ('inventario', 'departamento', 'descripcion', 'articulo', 'cantidad', 'observaciones')

#FORMULARIO DE ASIGNADO - ACTUALIZADO
class AsignacionEForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ('inventario', 'departamento', 'descripcion', 'articulo', 'cantidad', 'observaciones')