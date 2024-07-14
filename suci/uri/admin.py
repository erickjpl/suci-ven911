from django.contrib import admin
from .models import DiaSemana, Estados, Municipios, Parroquias, TraumaVehiculo, TraumaNoIntencional, EmergenciaNoTraumaticas, Resultados, EvaluacionRespiracion, IntervencionRespiracion, ResultadiRespiracion, ManiobraPelvis, ReaccionPupilar, HipotermiaOpcion, UnidadRespuestaInmediata

# Register your models here.

class DiaSemanaAdmin(admin.ModelAdmin):
    list_display = ('dia','created','updated')
    
    
class EstadosAdmin(admin.ModelAdmin):
    list_display = ('estado','created','updated')
    
class MunicipiosAdmin(admin.ModelAdmin):
    list_display = ('municipio','created','updated')
    
    
class ParroquiasAdmin(admin.ModelAdmin):
    list_display = ('parroquia','created','updated')
    
    
class TraumaVehiculoAdmin(admin.ModelAdmin):
    list_display = ('vehiculo','created','updated')
    
class TraumaNoIntencionalAdmin(admin.ModelAdmin):
    list_display = ('noIntencional','created','updated')
    
class EmergenciaNoTraumaticasAdmin(admin.ModelAdmin):
    list_display = ('emergencia','created','updated')
    
    
class ResultadosAdmin(admin.ModelAdmin):
    list_display = ('resultado','created','updated')
    
    
class EvaluacionRespiracionAdmin(admin.ModelAdmin):
    list_display = ('evaluacion','created','updated')
    
    
class IntervencionRespiracionAdmin(admin.ModelAdmin):
    list_display = ('intervencion','created','updated')
    
    
class ResultadiRespiracionAdmin(admin.ModelAdmin):
    list_display = ('resultado','created','updated')
    
class ManiobraPelvisAdmin(admin.ModelAdmin):
    list_display = ('maniobra','created','updated')
    
class ReaccionPupilarAdmin(admin.ModelAdmin):
    list_display = ('reaccion','created','updated')
    

class HipotermiaOpcionAdmin(admin.ModelAdmin):
    list_display = ('opcion','created','updated')
    
    
class UnidadRespuestaInmediataAdmin(admin.ModelAdmin):
    list_display = ('nroreporte','institucion')

admin.site.register(DiaSemana, DiaSemanaAdmin)
admin.site.register(Estados, EstadosAdmin)
admin.site.register(Municipios, MunicipiosAdmin)
admin.site.register(Parroquias, ParroquiasAdmin)
admin.site.register(TraumaVehiculo, TraumaVehiculoAdmin)
admin.site.register(TraumaNoIntencional, TraumaNoIntencionalAdmin)
admin.site.register(EmergenciaNoTraumaticas, EmergenciaNoTraumaticasAdmin)
admin.site.register(Resultados, ResultadosAdmin)
admin.site.register(EvaluacionRespiracion, EvaluacionRespiracionAdmin)
admin.site.register(IntervencionRespiracion, IntervencionRespiracionAdmin)
admin.site.register(ResultadiRespiracion, ResultadiRespiracionAdmin)
admin.site.register(ManiobraPelvis, ManiobraPelvisAdmin)
admin.site.register(ReaccionPupilar, ReaccionPupilarAdmin)
admin.site.register(HipotermiaOpcion, HipotermiaOpcionAdmin)
admin.site.register(UnidadRespuestaInmediata, UnidadRespuestaInmediataAdmin)