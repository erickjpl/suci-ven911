from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('uri', views.uri, name="uri"),
    #path('uri/update/<int:id>', views.update_uri, name="update_uri"),
    path('uri/<str:accion>/', views.Uri, name="uri"),
    #path('uri/obtener-datos-lugares-edicion/<int:lugar_id>/', views.obtener_datos_lugares_edicion, name='obtener-datos-lugares-edicion'),
    #   URLS DE MANTENIMIENTO MODULO URI
    path('uri/lugares/<str:accion>/', views.mantLugares, name="lugares"),
    path('uri/obtener-datos-lugares-edicion/<int:lugar_id>/', views.obtener_datos_lugares_edicion, name='obtener-datos-lugares-edicion'),
    path('uri/traslados/<str:accion>/', views.mantTraslados, name="traslados"),
    path('uri/obtener-datos-traslados-edicion/<int:traslado_id>/', views.obtener_datos_traslados_edicion, name='obtener-datos-traslados-edicion'),
    path('uri/reportes/<str:accion>/', views.mantReportes, name="reportes"),
    path('uri/obtener-datos-reportes-edicion/<int:reporte_id>/', views.obtener_datos_reportes_edicion, name='obtener-datos-reportes-edicion'),
    path('uri/servicios/<str:accion>/', views.mantServicios, name="servicios"),
    path('uri/obtener-datos-servicios-edicion/<int:servicio_id>/', views.obtener_datos_servicios_edicion, name='obtener-datos-servicios-edicion'),
    path('uri/tipoArma/<str:accion>/', views.mantTipoArma, name="tipoArma"),
    path('uri/obtener-datos-tipo-arma-edicion/<int:tipoA_id>/', views.obtener_datos_tipo_arma_edicion, name='obtener-datos-tipo-arma-edicion'),
    path('uri/tipoAccidente/<str:accion>/', views.mantTipoAccidente, name="tipoAccidente"),
    path('uri/obtener-datos-tipo-accidente-edicion/<int:tipoA_id>/', views.obtener_datos_tipo_accidente_edicion, name='obtener-datos-tipo-accidente-edicion'),
    path('uri/viajaba/<str:accion>/', views.mantViajaba, name="viajaba"),
    path('uri/colorPiel/<str:accion>/', views.mantColorPiel, name="colorPiel"),
    path('uri/temperaturaPiel/<str:accion>/', views.mantTemperaturaPiel, name="temperaturaPiel"),
    path('uri/humedadPiel/<str:accion>/', views.mantHumedadPiel, name="humedadPiel"),
    path('uri/evaluacion/<str:accion>/', views.mantEvaluacion, name="evaluacion"),
    path('uri/obtener-datos-evaluacion-edicion/<int:evaluacion_id>/', views.obtener_datos_evaluacion_edicion, name='obtener-datos-evaluacion-edicion'),
    path('uri/intervencion/<str:accion>/', views.mantIntervencion, name="intervencion"),
    path('uri/obtener-datos-intervencion-edicion/<int:intervencion_id>/', views.obtener_datos_intervencion_edicion, name='obtener-datos-intervencion-edicion'),
    path('uri/contacto/<str:accion>/', views.mantContactoPaciente, name="contacto"),
    path('uri/obtener-datos-contacto-edicion/<int:contacto_id>/', views.obtener_datos_contacto_edicion, name='obtener-datos-contacto-edicion'),
    path('uri/noContacto/<str:accion>/', views.mantNoContactoPaciente, name="noContacto"),
    
]