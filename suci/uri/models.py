from django.db import models
from rrhh.models import Sexo
# Create your models here.

class ContactoPaciente(models.Model):
    contacto = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "contacto"
        verbose_name_plural = "contactos"
        
    def __str__(self):
        return self.contacto
    
class NoContactoPaciente(models.Model):
    no_contacto = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "no_contacto"
        verbose_name_plural = "no_contactos"
        
    def __str__(self):
        return self.no_contacto
    
class Lugares(models.Model):
    lugar = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "lugar"
        verbose_name_plural = "lugares"
        
    def __str__(self):
        return self.lugar
    
    
class Traslado(models.Model):
    traslado = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "traslado"
        verbose_name_plural = "traslados"
        
    def __str__(self):
        return self.traslado
    
    
class Reportes(models.Model):
    reporte = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "via_reporte"
        verbose_name_plural = "via_reportes"
        
    def __str__(self):
        return self.reporte
    
    
class Servicios(models.Model):
    servicio = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "tipo_servicio"
        verbose_name_plural = "tipo_servicios"
        
    def __str__(self):
        return self.servicio
    
class Evaluacion(models.Model):
    evaluacion = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "evaluacion"
        verbose_name_plural = "evaluaciones"
        
    def __str__(self):
        return self.evaluacion
    
class Intervenciones(models.Model):
    intervencion = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "intervencion"
        verbose_name_plural = "intervenciones"
        
    def __str__(self):
        return self.intervencion
    
    
class Tipo_arma(models.Model):
    tipo_arma = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "tipo_arma"
        verbose_name_plural = "tipo_armas"
        
    def __str__(self):
        return self.tipo_arma
    
class TipoAccidente(models.Model):
    tipo_accidente = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "tipo_accidente"
        verbose_name_plural = "tipo_accidentes"
        
    def __str__(self):
        return self.tipo_accidente
    
class Viajaba(models.Model):
    viajaba = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "viajaba"
        verbose_name_plural = "viajabas"
        
    def __str__(self):
        return self.viajaba
    
class ColorPiel(models.Model):
    color_piel = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "color_piel"
        verbose_name_plural = "color_pieles"
        
    def __str__(self):
        return self.color_piel
    
class TemperaturaPiel(models.Model):
    temperatura_piel = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "temperatura_piel"
        verbose_name_plural = "temperatura_pieles"
        
    def __str__(self):
        return self.temperatura_piel
    
class HumedadPiel(models.Model):
    humedad_piel = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "humedad_piel"
        verbose_name_plural = "humedad_pieles"
        
    def __str__(self):
        return self.humedad_piel
    
    
class DiaSemana(models.Model):
    dia = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "dia"
        verbose_name_plural = "dias"
        
    def __str__(self):
        return self.dia
    
    
class Estados(models.Model):
    estado = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "estado"
        verbose_name_plural = "estados"
        
    def __str__(self):
        return self.estado
    
class Municipios(models.Model):
    municipio = models.CharField(max_length=15)
    estado= models.ForeignKey(Estados, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "municipio"
        verbose_name_plural = "municipios"
        
    def __str__(self):
        return self.municipio
    
class Parroquias(models.Model):
    parroquia = models.CharField(max_length=25)
    municipio= models.ForeignKey(Municipios, on_delete=models.CASCADE)
    estado= models.ForeignKey(Estados, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "parroquia"
        verbose_name_plural = "parroquias"
        
    def __str__(self):
        return self.parroquia

class TraumaVehiculo(models.Model):
    vehiculo = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "vehiculo"
        verbose_name_plural = "vehiculos"
        
    def __str__(self):
        return self.vehiculo
    
class TraumaNoIntencional(models.Model):
    noIntencional = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "no_intecional"
        verbose_name_plural = "no_intencionales"
        
    def __str__(self):
        return self.noIntencional
    

class EmergenciaNoTraumaticas(models.Model):
    emergencia = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "emergencia"
        verbose_name_plural = "emergencias"
        
    def __str__(self):
        return self.emergencia
    
class Resultados(models.Model):
    resultado = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "resultado"
        verbose_name_plural = "resultados"
        
    def __str__(self):
        return self.resultado
    
class EvaluacionRespiracion(models.Model):
    evaluacion = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "evaluacion"
        verbose_name_plural = "evaluaciones"
        
    def __str__(self):
        return self.evaluacion
    
    
class IntervencionRespiracion(models.Model):
    intervencion = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "intervencion"
        verbose_name_plural = "intervenciones"
        
    def __str__(self):
        return self.intervencion
    
class ResultadiRespiracion(models.Model):
    resultado = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "resultado"
        verbose_name_plural = "resultados"
        
    def __str__(self):
        return self.resultado
    
    
class ManiobraPelvis(models.Model):
    maniobra = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "maniobra"
        verbose_name_plural = "maniobras"
        
    def __str__(self):
        return self.maniobra
    
    
class ReaccionPupilar(models.Model):
    reaccion = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "reaccion"
        verbose_name_plural = "reacciones"
        
    def __str__(self):
        return self.reaccion
    
    
class HipotermiaOpcion(models.Model):
    opcion = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "hipotermia_opcion"
        verbose_name_plural = "hipotermia_opciones"
        
    def __str__(self):
        return self.opcion
    
    
class UnidadRespuestaInmediata(models.Model):
    fecha_atencion= models.DateField(verbose_name='Fecha de Atención', blank=True, null=True)
    nroreporte= models.CharField(max_length=10, blank=True, null=True)
    diareporte= models.ForeignKey(DiaSemana, on_delete=models.CASCADE, blank=True, null=True)
    placa= models.CharField(max_length=10, blank=True, null=True)
    institucion=models.CharField(max_length=300, blank=True, null=True)
    tipounidad=models.CharField(max_length=10, blank=True, null=True)
    num_interna=models.CharField(max_length=10, blank=True, null=True)
    nombre=models.CharField(max_length=50, blank=True, null=True)
    apellido=models.CharField(max_length=50, blank=True, null=True)
    genero=models.ForeignKey(Sexo, on_delete=models.CASCADE, related_name='uris_genero', blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    cedula=models.CharField(max_length=10, blank=True, null=True)
    nro_telefono=models.CharField(max_length=11, blank=True, null=True)
    direccion_paciente=models.CharField(max_length=300, blank=True, null=True)
    organismo1=models.CharField(max_length=20, blank=True, null=True)
    organismo2=models.CharField(max_length=20, blank=True, null=True)
    organismo3=models.CharField(max_length=20, blank=True, null=True)
    jefecomision1=models.CharField(max_length=50, blank=True, null=True)
    jefecomision2=models.CharField(max_length=50, blank=True, null=True)
    jefecomision3=models.CharField(max_length=50, blank=True, null=True)
    unidadplaca1=models.CharField(max_length=20, blank=True, null=True)
    unidadplaca2=models.CharField(max_length=20, blank=True, null=True)
    unidadplaca3=models.CharField(max_length=20, blank=True, null=True)
    firma1=models.CharField(max_length=20, blank=True, null=True)
    firma2=models.CharField(max_length=20, blank=True, null=True)
    firma3=models.CharField(max_length=20, blank=True, null=True)
    contactoPaciente=models.ForeignKey(ContactoPaciente, on_delete=models.CASCADE, blank=True, null=True)
    contactoNoPaciente=models.ForeignKey(NoContactoPaciente, on_delete=models.CASCADE, blank=True, null=True)
    centroAsistencial=models.CharField(max_length=50, blank=True, null=True)
    servicioAsistencial=models.CharField(max_length=50, blank=True, null=True)
    medicoRecibe=models.CharField(max_length=50, blank=True, null=True)
    msos=models.CharField(max_length=50, blank=True, null=True)
    regFotografico = models.BooleanField()
    nombreAcompanante=models.CharField(max_length=50, blank=True, null=True)
    apellidoAcompanante=models.CharField(max_length=50, blank=True, null=True)
    edadAcompanate = models.IntegerField(blank=True, null=True)
    parentezcoAcompanante=models.CharField(max_length=10, blank=True, null=True)
    cedulaAcompanante=models.CharField(max_length=10, blank=True, null=True)
    telefonoAcompanate=models.CharField(max_length=11, blank=True, null=True)
    generoAcompanante=models.ForeignKey(Sexo, on_delete=models.CASCADE, related_name='uris_genero_acompanante', blank=True, null=True )
    direccionAcompanante=models.CharField(max_length=300, blank=True, null=True)
    nombreTestigo=models.CharField(max_length=50, blank=True, null=True)
    apellidoTestigo=models.CharField(max_length=50, blank=True, null=True)
    edadTestigo = models.IntegerField(blank=True, null=True)
    cedulaTestigo=models.CharField(max_length=10, blank=True, null=True)
    telefonoTestigo=models.CharField(max_length=11, blank=True, null=True)
    direccionTestigo=models.CharField(max_length=300, blank=True, null=True)
    estadoEvento=models.ForeignKey(Estados, on_delete=models.CASCADE,blank=True, null=True)
    municipioEvento=models.ForeignKey(Municipios, on_delete=models.CASCADE, blank=True, null=True)
    parroquiaEvento=models.ForeignKey(Parroquias, on_delete=models.CASCADE, blank=True, null=True)
    sectorEvento=models.CharField(max_length=300, blank=True, null=True)
    calleEvento=models.CharField(max_length=300, blank=True, null=True)
    casaEvento=models.CharField(max_length=20, blank=True, null=True)
    pisoEvento=models.CharField(max_length=20, blank=True, null=True)
    referenciaEvento=models.CharField(max_length=300, blank=True, null=True)
    ejeEvento=models.CharField(max_length=30, blank=True, null=True)
    lugarAtencion=models.ForeignKey(Lugares, on_delete=models.CASCADE, blank=True, null=True)
    modotraslado=models.ForeignKey(Traslado, on_delete=models.CASCADE, blank=True, null=True)
    viaReporte=models.ForeignKey(Reportes, on_delete=models.CASCADE, blank=True, null=True)
    tipoServicio=models.ForeignKey(Servicios, on_delete=models.CASCADE, blank=True, null=True)
    horaAlarma = models.TimeField(blank=True, null=True)
    horaSalida = models.TimeField(blank=True, null=True)
    horaLlegada = models.TimeField(blank=True, null=True)
    hospital=models.CharField(max_length=50, blank=True, null=True)
    transferenciaEmergencia=models.CharField(max_length=50, blank=True, null=True)
    horaSede = models.TimeField(blank=True, null=True)
    tiempoServicio = models.CharField(max_length=50, blank=True, null=True)
    observacionesServicio = models.CharField(max_length=150, blank=True, null=True)
    accidenteVehicular = models.BooleanField(blank=True, null=True)
    tipoAccidente=models.ForeignKey(TipoAccidente, on_delete=models.CASCADE, blank=True, null=True)
    enfrentamientoArmado = models.BooleanField()
    tipoArma=models.ForeignKey(Tipo_arma, on_delete=models.CASCADE, blank=True, null=True)
    traumaVehiculo=models.ForeignKey(TraumaVehiculo, on_delete=models.CASCADE, blank=True, null=True)
    viajaba=models.ForeignKey(Viajaba, on_delete=models.CASCADE, blank=True, null=True)
    sustanciaPeligrosa = models.BooleanField()
    inflamable = models.BooleanField()
    explosivo = models.BooleanField()
    observacionesSustancia=models.CharField(max_length=100, blank=True, null=True)
    traumaNoIntencional=models.ForeignKey(TraumaNoIntencional, on_delete=models.CASCADE, blank=True, null=True)
    observacionesNo=models.CharField(max_length=100, blank=True, null=True)
    emergenciaMedica=models.ManyToManyField(EmergenciaNoTraumaticas, blank=True, null=True)
    hemorragia = models.BooleanField()
    presion = models.BooleanField()
    empaquetado = models.BooleanField()
    torniquete = models.BooleanField()
    evaluacion=models.ForeignKey(Evaluacion, on_delete=models.CASCADE, blank=True, null=True)
    intervencion=models.ForeignKey(Intervenciones, on_delete=models.CASCADE, blank=True, null=True)
    resultado=models.ForeignKey(Resultados, on_delete=models.CASCADE, blank=True, null=True)
    descripcionAdicional=models.CharField(max_length=100, blank=True, null=True)
    evaluacionResp=models.ManyToManyField(EvaluacionRespiracion,blank=True, null=True)
    intervencionResp=models.ManyToManyField(IntervencionRespiracion, blank=True, null=True)
    resultadoResp=models.ForeignKey(ResultadiRespiracion, on_delete=models.CASCADE, blank=True, null=True)
    descripcionAdicionalResultado=models.CharField(max_length=100, blank=True, null=True)
    colorPiel=models.ForeignKey(ColorPiel, on_delete=models.CASCADE, blank=True, null=True)
    temperaturaPiel=models.ForeignKey(TemperaturaPiel, on_delete=models.CASCADE, blank=True, null=True)
    humedadPiel=models.ForeignKey(HumedadPiel, on_delete=models.CASCADE, blank=True, null=True)
    pulso = models.BooleanField()
    otrasHerida= models.BooleanField()
    fractura= models.BooleanField()
    maniobraPelvis=models.ForeignKey(ManiobraPelvis, on_delete=models.CASCADE, blank=True, null=True)
    ecgO = models.IntegerField(blank=True, null=True)
    ecgV = models.IntegerField(blank=True, null=True)
    ecgM = models.IntegerField(blank=True, null=True)
    ecgTotal = models.IntegerField(blank=True, null=True)
    reaccionPupilar=models.ForeignKey(ReaccionPupilar, on_delete=models.CASCADE, blank=True, null=True)
    hipotermia = models.BooleanField()
    hipotermiaopcion=models.ManyToManyField(HipotermiaOpcion, blank=True, null=True)
    signosSintomas=models.CharField(max_length=100, blank=True, null=True)
    alergias=models.CharField(max_length=100, blank=True, null=True)
    medicamentos=models.CharField(max_length=100, blank=True, null=True)
    preexistencias=models.CharField(max_length=100, blank=True, null=True)
    ultimaComida=models.CharField(max_length=100, blank=True, null=True)
    evento=models.CharField(max_length=100, blank=True, null=True)
    horaMedicion=models.CharField(max_length=100, blank=True, null=True)
    frecuenciaCardiaca=models.CharField(max_length=100, blank=True, null=True)
    frecuenciaRespiratoria=models.CharField(max_length=100, blank=True, null=True)
    presionArterial=models.CharField(max_length=100, blank=True, null=True)
    spo2=models.CharField(max_length=100, blank=True, null=True)
    temperatura=models.CharField(max_length=100, blank=True, null=True)
    llenadoCapilar=models.CharField(max_length=100, blank=True, null=True)
    glicemiaCapilar=models.CharField(max_length=100, blank=True, null=True)
    escalaGlasgow=models.CharField(max_length=100, blank=True, null=True)
    medicamento1=models.CharField(max_length=100, blank=True, null=True)
    medicamento2=models.CharField(max_length=100, blank=True, null=True)
    medicamento3=models.CharField(max_length=100, blank=True, null=True)
    dosis1=models.CharField(max_length=100, blank=True, null=True)
    dosis2=models.CharField(max_length=100, blank=True, null=True)
    dosis3=models.CharField(max_length=100, blank=True, null=True)
    hora1 = models.TimeField(blank=True, null=True)
    hora2 = models.TimeField(blank=True, null=True)
    hora3 = models.TimeField(blank=True, null=True)
    resultadoEvaluacion=models.CharField(max_length=500, blank=True, null=True)
    trasladoIncial = models.BooleanField()
    hospitalOrigen=models.CharField(max_length=100, blank=True, null=True)
    medicoRefiere=models.CharField(max_length=100, blank=True, null=True)
    horaSalidaHosp = models.TimeField(blank=True, null=True)
    hospitalDestino=models.CharField(max_length=100, blank=True, null=True)
    horaLlegadaHosp = models.TimeField(blank=True, null=True)
    causa=models.CharField(max_length=100, blank=True, null=True)
    tecnicoEmergencia=models.CharField(max_length=50, blank=True, null=True)
    cedulaTecnico=models.CharField(max_length=10, blank=True, null=True)
    tercerTripulante=models.CharField(max_length=50, blank=True, null=True)
    cedulaTripulante=models.CharField(max_length=10, blank=True, null=True)
    conductorUnidad=models.CharField(max_length=50, blank=True, null=True)
    cedulaConductor=models.CharField(max_length=10, blank=True, null=True)
    supervisorGuardia=models.CharField(max_length=50, blank=True, null=True)
    cedulaSupervisor=models.CharField(max_length=10, blank=True, null=True)
    medicoGuardia=models.CharField(max_length=50, blank=True, null=True)
    cedulaMedico=models.CharField(max_length=10, blank=True, null=True)
    selloMsds=models.CharField(max_length=25, blank=True, null=True)
    
    class Meta:
        verbose_name='uri'
        verbose_name_plural='uris'

    def __str__(self):
        return self.nroreporte    