from django import forms
from .models import  Incidencias

# FORMULARIO DE INCIDENCIAS
class IncidenciasForm(forms.ModelForm):
    class Meta:
        model = Incidencias
        fields = ('estado', 'sede', 'departamento', 'tipoincidencia', 'usuario', 'observaciones', 'tiposolicitud')

# FORMULARIO DE ACTUALIZACIÓN DE INCIDENCIAS
class IncidenciasEForm(forms.ModelForm):
    class Meta:
        model = Incidencias
        fields = ('estado', 'sede', 'departamento', 'tipoincidencia', 'usuario', 'observaciones', 'tiposolicitud')
