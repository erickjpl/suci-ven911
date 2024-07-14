from django import forms
from .models import  UnidadRespuestaInmediata, Lugares, Traslado, Reportes, Servicios, Tipo_arma, TipoAccidente, Viajaba, ColorPiel, TemperaturaPiel, HumedadPiel, Evaluacion, Intervenciones, ContactoPaciente, NoContactoPaciente

# FORMULARIO DE INCIDENCIAS
# FORMULARIO DE URI
class UriForm(forms.ModelForm):
    class Meta:
        model = UnidadRespuestaInmediata
        fields = (
            'fecha_atencion',
            'nroreporte',
            'diareporte',
            'placa', 
            'institucion', 
            'tipounidad', 
            'num_interna', 
            'nombre', 
            'apellido', 
            'genero', 
            'edad',
            'cedula', 
            'nro_telefono', 
            'direccion_paciente',
            'organismo1',
            'organismo2',
            'organismo3',
            'jefecomision1', 
            'jefecomision2', 
            'jefecomision3', 
            'unidadplaca1', 
            'unidadplaca2', 
            'unidadplaca3', 
            'firma1', 
            'firma2',
            'firma3', 
            'contactoPaciente', 
            'contactoNoPaciente',
            'centroAsistencial',
            'servicioAsistencial',
            'medicoRecibe',
            'msos', 
            'regFotografico', 
            'nombreAcompanante', 
            'apellidoAcompanante', 
            'edadAcompanate', 
            'parentezcoAcompanante', 
            'cedulaAcompanante', 
            'telefonoAcompanate',
            'generoAcompanante', 
            'direccionAcompanante', 
            'nombreTestigo',
            'apellidoTestigo',
            'edadTestigo',
            'cedulaTestigo', 
            'telefonoTestigo', 
            'direccionTestigo', 
            'estadoEvento', 
            'municipioEvento', 
            'parroquiaEvento', 
            'sectorEvento', 
            'calleEvento',
            'casaEvento', 
            'pisoEvento', 
            'referenciaEvento',
            'ejeEvento',
            'lugarAtencion',
            'modotraslado',
            'viaReporte', 
            'tipoServicio', 
            'horaAlarma', 
            'horaSalida', 
            'horaLlegada', 
            'hospital', 
            'transferenciaEmergencia', 
            'horaSede',
            'tiempoServicio', 
            'observacionesServicio', 
            'accidenteVehicular',
            'tipoAccidente',
            'enfrentamientoArmado',
            'tipoArma',
            'traumaVehiculo', 
            'viajaba', 
            'sustanciaPeligrosa', 
            'inflamable', 
            'explosivo', 
            'observacionesSustancia', 
            'traumaNoIntencional', 
            'observacionesNo',
            'emergenciaMedica', 
            'hemorragia', 
            'presion',
            'empaquetado',
            'torniquete',
            'evaluacion',
            'intervencion', 
            'resultado', 
            'descripcionAdicional', 
            'evaluacionResp', 
            'intervencionResp', 
            'resultadoResp', 
            'descripcionAdicionalResultado', 
            'colorPiel',
            'temperaturaPiel', 
            'humedadPiel', 
            'pulso',
            'otrasHerida',
            'fractura',
            'maniobraPelvis',
            'ecgO', 
            'ecgV', 
            'ecgM', 
            'ecgTotal', 
            'reaccionPupilar', 
            'hipotermia', 
            'hipotermiaopcion', 
            'signosSintomas',
            'alergias', 
            'medicamentos', 
            'preexistencias',
            'ultimaComida', 
            'evento',
            'horaMedicion', 
            'frecuenciaCardiaca', 
            'frecuenciaRespiratoria',
            'presionArterial',
            'spo2',
            'temperatura',
            'llenadoCapilar', 
            'glicemiaCapilar', 
            'escalaGlasgow', 
            'medicamento1', 
            'medicamento2', 
            'medicamento3', 
            'dosis1', 
            'dosis2',
            'dosis3', 
            'hora1', 
            'hora2',
            'hora3',
            'resultadoEvaluacion',
            'trasladoIncial',
            'hospitalOrigen', 
            'medicoRefiere', 
            'horaSalidaHosp', 
            'hospitalDestino', 
            'horaLlegadaHosp', 
            'causa', 
            'tecnicoEmergencia', 
            'cedulaTecnico',
            'tercerTripulante',
            'cedulaTripulante', 
            'conductorUnidad', 
            'cedulaConductor', 
            'supervisorGuardia', 
            'cedulaSupervisor', 
            'medicoGuardia', 
            'cedulaMedico', 
            'selloMsds',
            )

# FORMULARIO DE ACTUALIZACIÓN DE URI
class UriEForm(forms.ModelForm):
    class Meta:
        model = UnidadRespuestaInmediata
        fields = ('fecha_atencion', 'nroreporte', 'diareporte', 'placa', 'institucion', 'tipounidad', 'num_interna', 'nombre', 'apellido', 'genero', 'cedula', 'nro_telefono', 'direccion_paciente')

class FormContactoPaciente(forms.ModelForm):
    class Meta:
        model = ContactoPaciente
        fields = ['contacto', 'id' ]

class FormNoContactoPaciente(forms.ModelForm):
    class Meta:
        model = NoContactoPaciente
        fields = ['no_contacto', 'id' ]


class FormLugares(forms.ModelForm):

    class Meta:
        model = Lugares
        fields = ['lugar', 'id' ]
        
class FormTraslado(forms.ModelForm):

    class Meta:
        model = Traslado
        fields = ['traslado', 'id' ]
        
        
class FormReportes(forms.ModelForm):

    class Meta:
        model = Reportes
        fields = ['reporte', 'id' ]
        
        
class FormServicios(forms.ModelForm):

    class Meta:
        model = Servicios
        fields = ['servicio', 'id' ]

class FormTipoArma(forms.ModelForm):

    class Meta:
        model = Tipo_arma
        fields = ['tipo_arma', 'id' ]

class FormTipoAccidente(forms.ModelForm):

    class Meta:
        model = TipoAccidente
        fields = ['tipo_accidente', 'id' ]
        
class FormViajaba(forms.ModelForm):

    class Meta:
        model = Viajaba
        fields = ['viajaba', 'id' ]

class FormColorPiel(forms.ModelForm):
    class Meta:
        model = ColorPiel
        fields = ['color_piel', 'id' ]

class FormTemperaturaPiel(forms.ModelForm):
    class Meta:
        model = TemperaturaPiel
        fields = ['temperatura_piel', 'id' ]

class FormHumedadPiel(forms.ModelForm):
    class Meta:
        model = HumedadPiel
        fields = ['humedad_piel', 'id' ]

class FormEvaluacion(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['evaluacion', 'id' ]

class FormIntervencion(forms.ModelForm):
    class Meta:
        model = Intervenciones
        fields = ['intervencion', 'id' ]

