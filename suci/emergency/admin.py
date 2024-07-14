from django.contrib import admin
from .models import CuadrantePaz
from .models import Estado
from .models import Municipio
from .models import Parroquia
from .models import Incidencia
from .models import OrganismoCompetente
from .models import Emergency

class EmergencyAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", )

# Register your models here.
admin.site.register(CuadrantePaz)
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Parroquia)
admin.site.register(Incidencia)
admin.site.register(OrganismoCompetente)
admin.site.register(Emergency, EmergencyAdmin)
