from django.contrib import admin
from .models import Incidencias
# Register your models here.
class IncidenciasAdmin(admin.ModelAdmin):
    list_display = ('estado', 'sede', 'departamento', 'tipoincidencia', 'usuario', 'observaciones', 'tiposolicitud')
    
admin.site.register(Incidencias, IncidenciasAdmin)