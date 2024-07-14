from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('personal/<str:accion>/', views.personal, name="ingresosPersonal"),
    path('generar-pdf/', views.generar_pdf, name='generar-pdf'),
    path('personalRetirado/', views.personalRetirado, name="personalRetirado"),
    path('generar-pdf-retirados/', views.generar_pdf_retirados, name='generar-pdf-retirados'),
    path('personalVacaciones/', views.personalVacaciones, name="personalVacaciones"),
    path('generar-pdf-vacaciones/', views.generar_pdf_vacaciones, name='generar-pdf-vacaciones'),
    path('descargar-excel/', views.descargar_excel, name='descargar-excel'),
    path('descargar-excel-retirados/', views.descargar_excel_retirados, name='descargar-excel-retirados'),
    path('descargar-excel-vacaciones/', views.descargar_excel_vacaciones, name='descargar-excel-vacaciones'),
    path('movimiento-personal/', views.movimientoPersonal, name="movimiento-personal"),
    path('consulta-personal/', views.consultaPersonal, name="consulta-personal"),
    path('obtener-datos-edicion/<int:personal_id>/', views.obtener_datos_edicion, name='obtener-datos-edicion'),
    path('obtener-datos/<int:personal_id>/', views.obtener_datos, name='obtener-datos'),
    path('bienes/<str:accion>/<int:departamentofilter>/', views.bienes, name='bienes'),
    path('obtener-datos-bienes-edicion/<int:bienes_id>/', views.obtener_datos_bienes_edicion, name='obtener-datos-bienes-edicion'),
    path('descargar-excel-bienes/', views.descargar_excel_bienes, name='descargar-excel-bienes'),
    path('generar-pdf-bienes/', views.generar_pdf_bienes, name='generar-pdf-bienes'),
    path('sueldos/', views.sueldos, name="sueldos"),
    path('generar-pdf-sueldos/', views.generar_pdf_sueldos, name='generar-pdf-sueldos'),
    path('descargar-excel-sueldos/', views.descargar_excel_sueldos, name='descargar-excel-sueldos'),
    path('obtener-datos-sueldos-edicion/<int:sueldo_id>/', views.obtener_datos_sueldos_edicion, name='obtener-datos-sueldos-edicion'),
    # URLS DE MANTENIMIENTO
    path('estadocivil/', views.estadoCivil, name="estadoCivil"),
    path('genero/', views.mantSexo, name="genero"),
    path('tallaCamisa/<str:accion>/', views.mantTallaCamisa, name="tallaCamisa"),
    path('obtener-datos-tallaC-edicion/<int:tallaC_id>/', views.obtener_datos_tallaC_edicion, name='obtener-datos-tallaC-edicion'),
    path('tallaPantalon/<str:accion>/', views.mantTallaPantalon, name="tallaPantalon"),
    path('obtener-datos-tallaP-edicion/<int:tallaP_id>/', views.obtener_datos_tallaP_edicion, name='obtener-datos-tallaP-edicion'),
    path('tallaZapato/<str:accion>/', views.mantTallaZapato, name="tallaZapato"),
    path('obtener-datos-tallaZ-edicion/<int:tallaZ_id>/', views.obtener_datos_tallaZ_edicion, name='obtener-datos-tallaZ-edicion'),
    path('gradoInstruccion/', views.mantGrado, name="gradoInstruccion"),
    path('tipoPersonal/', views.mantTipoPersonal, name="tipoPersonal"),
    path('cargo/<str:accion>/', views.mantCargo, name="cargo"),
    path('obtener-datos-cargo-edicion/<int:cargoE_id>/', views.obtener_datos_cargo_edicion, name='obtener-datos-cargo-edicion'),
    path('departamento/<str:accion>/', views.mantDepartamento, name="departamento"),
    path('obtener-datos-departamento-edicion/<int:departamento_id>/', views.obtener_datos_departamento_edicion, name='obtener-datos-departamento-edicion'),
    path('sedes/<str:accion>/', views.mantSedes, name="sede"),
    path('obtener-datos-sede-edicion/<int:sede_id>/', views.obtener_datos_sede_edicion, name='obtener-datos-sede-edicion'),
    path('bonoguerra/<str:accion>/', views.mantBonoGuerra, name="bonoguerra"),
    path('obtener-datos-bono-edicion/<int:bono_id>/', views.obtener_datos_bono_edicion, name='obtener-datos-bono-edicion'),
    path('cestaticket/<str:accion>/', views.mantCestaTicket, name="cestaticket"),
    path('obtener-datos-cestaticket-edicion/<int:cesta_id>/', views.obtener_datos_cestaticket_edicion, name='obtener-datos-cestaticket-edicion'),
    path('sueldominimo/<str:accion>/', views.mantSueldoMinimo, name="sueldominimo"),
    path('obtener_datos_sueldominimo_edicion/<int:sueldo_id>/', views.obtener_datos_sueldominimo_edicion, name='obtener_datos_sueldominimo_edicion'),
    path('primaprofesional/<str:accion>/', views.mantPrimaProfesional, name="primaprofesional"),
    path('obtener_datos_prima_edicion/<int:prima_id>/', views.obtener_datos_prima_edicion, name='obtener_datos_prima_edicion'),
    #URLS NOMINA 
    #URLS NOMINA 
    
    
]

