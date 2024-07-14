from django import forms
from django.forms import ModelForm
from .models import *
from .models import Objetivos, Actividades, Llamadas, Infraestructura

# FORMULARIO DE PLANIFICACION
class ObjetivosForm(forms.ModelForm):
    fechai = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    fechaf = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Objetivos
        fields = ('fechai', 'fechaf', 'objetiv', 'meta',)

# FORMULARIO DE ACTUALIZACIÓN DE PLANIFICACION
class ObjetivosUForm(forms.ModelForm):
    fechai = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    fechaf = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Objetivos        
        fields = ('fechai', 'fechaf', 'objetiv', 'meta',)

# FORMULARIO DE PLANIFICACION
class ActividadesForm(forms.ModelForm):
    fechai = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    fechaf = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Actividades
        fields = ('fechai', 'fechaf', 'objetiv', 'meta',)

# FORMULARIO DE ACTUALIZACIÓN DE PLANIFICACION
class ActividadesUForm(forms.ModelForm):
    fechai = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    fechaf = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Actividades        
        fields = ('fechai', 'fechaf', 'objetiv', 'meta',)

class LlamadasForm(forms.ModelForm):
    class Meta:
        model = Llamadas        
        fields = ('estado', 'mes', 'informativa', 'falsa', 'realesno', 'realesf', 'videop')

class LlamadasUForm(forms.ModelForm):
    class Meta:
        model = Llamadas        
        fields = ('estado', 'mes', 'informativa', 'falsa', 'realesno', 'realesf', 'videop')

class InfraestructuraForm(forms.ModelForm):
    class Meta:
        model = Infraestructura        
        fields = ('estado', 'mes', 'infraestructura', 'cantidad')

class InfraestructuraEForm(forms.ModelForm):
    class Meta:
        model = Infraestructura        
        fields = ('estado', 'mes', 'infraestructura', 'cantidad')
