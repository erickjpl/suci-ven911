from django.contrib import admin
from .models import Personal, Nacionalidad, Sexo, EstadoCivil, Sangre, TallasCamisa, TallasPantalon, TallasZapatos, Grado, TipoPersonal, Cargo, Departamento, Sedes, Bienes, Sueldos, CestaTicket, BonoGuerra, Tasa, PrimaProfesionalismo, SueldoMinimo

# Register your models here.


class PersonalAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'nacionalidad', 'cedula', 'departamento', 'cargo') #   Campos a ver en cPanel
    search_fields = ('nombres', 'apellidos', 'cedula') 
    list_filter = ('nacionalidad', 'sexo', 'estado_civil', 'tipo_sangre', 'grado_instruccion', 'tipo_personal', 'fecha_ingreso_911', 'fecha_ingreso_apn', 'departamento', 'cargo', 'sede')     
    date_hierarchy = 'fecha_ingreso_911'  
    readonly_fields = ("created", "updated")
    
    
class BienesAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    
class NacionalidadAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

    
class SexoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    
class EstadoCivilAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    
class SangreAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    
class TallaCamisaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    
class TallaPantalonAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    
class TallaZapatoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    
class GradoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    
class TipoPersonalAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    
class CargoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    
class DepartamentoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    
class SedeAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    
class SueldosAdmin(admin.ModelAdmin):
    list_display = ('personal', 'sueldo_base')
    
    
class CestaTicketAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'monto')
    

class BonoGuerraAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'monto')
    
    
class TasaAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'monto')
    

class PrimaProfesionalismoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'porcentaje')
    
class SueldoMinimoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'monto')

admin.site.register(Personal, PersonalAdmin)
admin.site.register(Nacionalidad, NacionalidadAdmin)
admin.site.register(Sexo, SexoAdmin)
admin.site.register(EstadoCivil, EstadoCivilAdmin)
admin.site.register(Sangre, SangreAdmin)
admin.site.register(TallasCamisa, TallaCamisaAdmin)
admin.site.register(TallasPantalon, TallaPantalonAdmin)
admin.site.register(TallasZapatos, TallaZapatoAdmin)
admin.site.register(Grado, GradoAdmin)
admin.site.register(TipoPersonal, TipoPersonalAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Sedes, SexoAdmin)
admin.site.register(Bienes, BienesAdmin)
admin.site.register(Sueldos, SueldosAdmin)
admin.site.register(CestaTicket, CestaTicketAdmin)
admin.site.register(BonoGuerra, BonoGuerraAdmin)
admin.site.register(Tasa, TasaAdmin)
admin.site.register(PrimaProfesionalismo, PrimaProfesionalismoAdmin)
admin.site.register(SueldoMinimo, SueldoMinimoAdmin)

