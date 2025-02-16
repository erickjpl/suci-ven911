from django.urls import include, path
from .views import SeguridadView

urlpatterns = [
    path("", SeguridadView.as_view(), name="seguridad",),
    path("entradas/", include(("apps.seguridad.entradas.urls", "entradas"))),
    path("api/entradas/",include(("apps.seguridad.entradas.urls_apis", "api_entradas")),),
    path("gestion/", include(("apps.seguridad.gestiones.urls", "gestion"))),
    path("api/gestion/",include(("apps.seguridad.gestiones.urls_apis", "api_gestion")),),
    path("salida/", include(("apps.seguridad.salidas.urls", "salida"))),
    path("api/salida/",include(("apps.seguridad.salidas.urls_apis", "api_salida")),),
    path("vehiculo/", include(("apps.seguridad.vehiculos.urls", "vehiculo"))),
    path("api/vehiculo/",include(("apps.seguridad.vehiculos.urls_apis", "api_vehiculo")),),
]