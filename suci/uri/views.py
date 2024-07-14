from django.shortcuts import render, redirect
from django.http import FileResponse, Http404, JsonResponse
from .forms import UriForm, UriEForm, FormLugares, FormTraslado, FormReportes, FormServicios, FormTipoArma, FormTipoAccidente, FormViajaba, FormColorPiel, FormTemperaturaPiel, FormHumedadPiel, FormEvaluacion, FormIntervencion, FormContactoPaciente, FormNoContactoPaciente
from .models import UnidadRespuestaInmediata, Lugares, Traslado, Reportes, Servicios, Tipo_arma, TipoAccidente, Viajaba, ColorPiel, TemperaturaPiel, HumedadPiel, Evaluacion, Intervenciones, ContactoPaciente, NoContactoPaciente, DiaSemana, Sexo, Estados, Municipios, Parroquias, TraumaVehiculo, TraumaNoIntencional, EmergenciaNoTraumaticas, Resultados, EvaluacionRespiracion, IntervencionRespiracion, ResultadiRespiracion, ManiobraPelvis, ReaccionPupilar, HipotermiaOpcion

# Create your views here.
def Uri(request, accion):

    uri = UnidadRespuestaInmediata.objects.all()
    
    if accion == 'todos':
        form = UriForm()

    #   AGREGAR CONTACTO
    if accion == 'agregar':
        print ("Hola1")
        if request.method =='POST':
            print ("Hola2")
            form = UriForm(request.POST)
            print ("Hola3")
            if form.is_valid():
                print ("Hola4")
                form.save()
                print ("Hola5")
                return redirect('/uri/todos')
            else:
                print("Formulario no valido")
                for field in form:
                    for error in field.errors:
                        print(f"Error en campo {field.label}: {error}")
    dias = DiasSemana()
    generos = GeneroPaciente()
    consultas = consulPaciente()
    noContacto = noContactoPaciente()
    generosA = GeneroAcompanante()
    estado = EstadosEvento()
    municipios = MunicipiosEvento()
    parroquias = ParroquiasEvento()
    lugares = lugarAtencion()
    traslados = ModoTraslado()
    reportes = ViaReporte()
    servicios = TipoServicio()
    accidentes = TipoAccidentes()
    armas = TipoArma()
    vehiculos = traumaVehiculo()
    viajabas = Viajabas()
    traumas = TrumanoIntencional()
    emergencias = emergenciasMedicasNoTraumaticas()
    evaluaciones = EvaluacionViaAerea()
    intervenciones = IntervencionViaAerea()
    resultados = ResultadoViaAerea()
    evaluacionesRespiracion = evaluacionRespiracion()
    intervencionesRespiracion = intervencionRespiracion()
    resultadosRespiracion = resultadoRespiracion()
    colores = colorPiel()
    temperaturas = temperaturaPiel()
    humedades = humedadPiel()
    maniobras = maniobrasPelvis()
    reacciones = reaccionPupilar()
    opciones = opcionHipotermiar()
    context = {
        "dias": dias, 
        "generos": generos, 
        "consultas": consultas,
        "noContacto": noContacto,
        "generosA": generosA,
        "estado": estado,
        "parroquias": parroquias,
        "municipios": municipios,
        "lugares": lugares,
        "traslados": traslados,
        "reportes": reportes,
        "servicios": servicios,
        "accidentes": accidentes,
        "armas": armas,
        "vehiculos": vehiculos,
        "viajabas": viajabas,
        "traumas": traumas,
        "emergencias": emergencias,
        "evaluaciones": evaluaciones,
        "intervenciones": intervenciones,
        "resultados": resultados,
        "evaluacionesRespiracion": evaluacionesRespiracion,
        "intervencionesRespiracion": intervencionesRespiracion,
        "resultadosRespiracion": resultadosRespiracion,
        "colores": colores,
        "temperaturas": temperaturas,
        "humedades": humedades,
        "maniobras": maniobras,
        "reacciones": reacciones,
        "opciones": opciones,
        "uri": uri,
        "form": form
    }

    return render(request, 'uri.html', context)



def uribk(request):
    if request.method == 'POST':
        formpi = UriForm(request.POST)
        if formpi.is_valid():
            formpi.save()
        else:
            context = {'formpi': formpi}
            return render(request, 'uri.html', context)
    uri = UnidadRespuestaInmediata.objects.all()
    context = {'formpi': UriForm(), 'formegh': UriEForm(), 'urii': uri}
    return render(request, 'uri.html', context)


# VISTAS DE ACTUALIZACIÓN DE URI
def update_uri(request, id):
    queryset = UnidadRespuestaInmediata.objects.get(id=id)
    form = UriEForm(instance=queryset)
    if request.method == 'POST':
        form = UriEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/uri#updatesuccess')
        
    #VISTAS DE CONTACTO CON EL PACIENTE
def mantContactoPaciente(request, accion):

    contacto = ContactoPaciente.objects.all()
    
    if accion == 'todos':
        form = FormContactoPaciente()

    #   AGREGAR CONTACTO
    if accion == 'agregar':
        if request.method =='POST':
            form = FormContactoPaciente(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/uri/contacto/todos')

    #EDITAR CONTACTO
    if accion == 'editar':
        if request.method == 'POST':
            form = FormContactoPaciente(request.POST)
            if form.is_valid():
                id_m =  request.POST["id"]
                contacto_m = form.cleaned_data['contacto']
                
                try:
                    contactos = ContactoPaciente.objects.get(id=id_m)
                except ContactoPaciente.DoesNotExist:
                    raise ValueError("Evaluación no existe.")
                    
                contactos.contacto = contacto_m
                contactos.save()
        else:
             
             form = FormContactoPaciente()
            
    
    context = {
        "contacto": contacto,
        "form": form
    }

    return render(request, "mantenimientosUri/contactoPaciente.html", context)


def obtener_datos_contacto_edicion(request, contacto_id):
    try:
        contacto = ContactoPaciente.objects.get(id=contacto_id)
        data = {
            'id': contacto.id,
            'contacto': contacto.contacto,
            # Agrega más campos según sea necesario
        }
        return JsonResponse(data)
    except ContactoPaciente.DoesNotExist:
        return JsonResponse({'error': 'Registro no encontrado'}, status=404)
    
    # VISTAS DE NO CONTACTO CON EL PACIENTE
def mantNoContactoPaciente(request, accion):

    no_contacto = NoContactoPaciente.objects.all()
    
    if accion == 'todos':
        form = FormNoContactoPaciente()

    #   AGREGAR CONTACTO
    if accion == 'agregar':
        if request.method =='POST':
            form = FormNoContactoPaciente(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/uri/noContacto/todos')

    #EDITAR CONTACTO
    if accion == 'editar':
        if request.method == 'POST':
            form = FormNoContactoPaciente(request.POST)
            if form.is_valid():
                id_m =  request.POST["id"]
                no_contacto_m = form.cleaned_data['no_contacto']
                
                try:
                    contactos = NoContactoPaciente.objects.get(id=id_m)
                except NoContactoPaciente.DoesNotExist:
                    raise ValueError("Evaluación no existe.")
                    
                contactos.contacto = no_contacto_m
                contactos.save()
        else:
             
             form = FormNoContactoPaciente()
            
    
    context = {
        "no_contacto": no_contacto,
        "form": form
    }

    return render(request, "mantenimientosUri/NoContactoPaciente.html", context)

        
#   VISTA DE MANTENIMIENTO DE LUGARES DE ATENCION
def mantLugares(request, accion):

    lugares = Lugares.objects.all()
    
    if accion == 'todos':
        form = FormLugares()

    #   AGREGAR LUGAR 
    if accion == 'agregar':
        if request.method =='POST':
            form = FormLugares(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/uri/lugares/todos')

    #EDITAR LUGAR    
    if accion == 'editar':
        if request.method == 'POST':
            form = FormLugares(request.POST)
            if form.is_valid():
                id_m =  request.POST["id"]
                lugar_m = form.cleaned_data['lugar']
                
                try:
                    lugar = Lugares.objects.get(id=id_m)
                except Lugares.DoesNotExist:
                    raise ValueError("Lugar no existe.")
                    
                lugar.lugar = lugar_m
                lugar.save()
        else:
             
             form = FormLugares()
            
    
    context = {
        "lugares": lugares,
        "form": form
    }

    return render(request, "mantenimientosUri/lugares.html", context)


def obtener_datos_lugares_edicion(request, lugar_id):
    try:
        lugar = Lugares.objects.get(id=lugar_id)
        data = {
            'id': lugar.id,
            'lugar': lugar.lugar,
            # Agrega más campos según sea necesario
        }
        return JsonResponse(data)
    except Lugares.DoesNotExist:
        return JsonResponse({'error': 'Registro no encontrado'}, status=404)

    #VISTAS DE TRASLADOS 
def mantTraslados(request, accion):

    traslados = Traslado.objects.all()
    
    if accion == 'todos':
        form = FormTraslado()

    #   AGREGAR TRASLADO
    if accion == 'agregar':
        if request.method =='POST':
            form = FormTraslado(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/uri/traslados/todos')

    #EDITAR TRASLADO   
    if accion == 'editar':
        if request.method == 'POST':
            form = FormTraslado(request.POST)
            if form.is_valid():
                id_m =  request.POST["id"]
                trasaldo_m = form.cleaned_data['traslado']
                
                try:
                    traslado = Traslado.objects.get(id=id_m)
                except Lugares.DoesNotExist:
                    raise ValueError("Lugar no existe.")
                    
                traslado.traslado = trasaldo_m
                traslado.save()
        else:
             
             form = FormTraslado()
            
    
    context = {
        "traslados": traslados,
        "form": form
    }

    return render(request, "mantenimientosUri/traslados.html", context)


def obtener_datos_traslados_edicion(request, traslado_id):
    try:
        traslado = Traslado.objects.get(id=traslado_id)
        data = {
            'id': traslado.id,
            'traslado': traslado.traslado,
            # Agrega más campos según sea necesario
        }
        return JsonResponse(data)
    except Lugares.DoesNotExist:
        return JsonResponse({'error': 'Registro no encontrado'}, status=404)

    #VISTAS DE REPORTES 
def mantReportes(request, accion):

    reportes = Reportes.objects.all()
    
    if accion == 'todos':
        form = FormReportes()

    #   AGREGAR REPORTE
    if accion == 'agregar':
        if request.method =='POST':
            form = FormReportes(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/uri/reportes/todos')

    #EDITAR REPORTE    
    if accion == 'editar':
        if request.method == 'POST':
            form = FormReportes(request.POST)
            if form.is_valid():
                id_m =  request.POST["id"]
                reporte_m = form.cleaned_data['reporte']
                
                try:
                    reporte = Reportes.objects.get(id=id_m)
                except Reportes.DoesNotExist:
                    raise ValueError("Reporte no existe.")
                    
                reporte.reporte = reporte_m
                reporte.save()
        else:
             
             form = FormReportes()
            
    
    context = {
        "reportes": reportes,
        "form": form
    }

    return render(request, "mantenimientosUri/reportes.html", context)


def obtener_datos_reportes_edicion(request, reporte_id):
    try:
        reporte = Reportes.objects.get(id=reporte_id)
        data = {
            'id': reporte.id,
            'reporte':reporte.reporte,
            # Agrega más campos según sea necesario
        }
        return JsonResponse(data)
    except Reportes.DoesNotExist:
        return JsonResponse({'error': 'Registro no encontrado'}, status=404)
    
    #VISTAS DE MANTENIEMIENTO DE SERVICIOS
def mantServicios(request, accion):

    servicios = Servicios.objects.all()
    
    if accion == 'todos':
        form = FormServicios()

    #   AGREGAR SERVICIO
    if accion == 'agregar':
        if request.method =='POST':
            form = FormServicios(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/uri/servicios/todos')

    #EDITAR  SERVICIO    
    if accion == 'editar':
        if request.method == 'POST':
            form = FormServicios(request.POST)
            if form.is_valid():
                id_m =  request.POST["id"]
                servicio_m = form.cleaned_data['servicio']
                
                try:
                    servicio = Servicios.objects.get(id=id_m)
                except Servicios.DoesNotExist:
                    raise ValueError("Servicios no existe.")
                    
                servicio.servicio = servicio_m
                servicio.save()
        else:
             
             form = FormServicios()
            
    
    context = {
        "servicios": servicios,
        "form": form
    }

    return render(request, "mantenimientosUri/servicios.html", context)


def obtener_datos_servicios_edicion(request, servicio_id):
    try:
        servicio = Servicios.objects.get(id=servicio_id)
        data = {
            'id': servicio.id,
            'servicio': servicio.servicio,
            # Agrega más campos según sea necesario
        }
        return JsonResponse(data)
    except Reportes.DoesNotExist:
        return JsonResponse({'error': 'Registro no encontrado'}, status=404)
    #VISTAS DE MANTENIMIENTOS DE TIPO DE ARMA 
def mantTipoArma(request, accion):

    tipo_arma = Tipo_arma.objects.all()
    
    if accion == 'todos':
        form = FormTipoArma()

    #   AGREGAR TIPO DE ARMA  
    if accion == 'agregar':
        if request.method =='POST':
            form = FormTipoArma(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/uri/tipoArma/todos')

    #EDITAR TIPO DE ARMA     
    if accion == 'editar':
        if request.method == 'POST':
            form = FormTipoArma(request.POST)
            if form.is_valid():
                id_m =  request.POST["id"]
                tipo_arma_m = form.cleaned_data['tipo_arma']
                
                try:
                    tipoA = Tipo_arma.objects.get(id=id_m)
                except Tipo_arma.DoesNotExist:
                    raise ValueError("Registro no existe.")
                    
                tipoA.tipo_arma = tipo_arma_m
                tipoA.save()
        else:
             
             form = FormTipoArma()
            
    
    context = {
        "tipo_arma": tipo_arma,
        "form": form
    }

    return render(request, "mantenimientosUri/tipo_arma.html", context)


def obtener_datos_tipo_arma_edicion(request, tipoA_id):
    try:
        tipoA = Tipo_arma.objects.get(id=tipoA_id)
        data = {
            'id': tipoA.id,
            'tipo_arma': tipoA.tipo_arma,
            # Agrega más campos según sea necesario
        }
        return JsonResponse(data)
    except Tipo_arma.DoesNotExist:
        return JsonResponse({'error': 'Registro no encontrado'}, status=404)
    
        #VISTAS DE MANTENIMIENTOS DE TIPO DE ACCIDENTE 

def mantTipoAccidente(request, accion):

    tipo_accidentes = TipoAccidente.objects.all()
    
    if accion == 'todos':
        form = FormTipoAccidente()

    #   AGREGAR TIPO DE ACCIDENTE  
    if accion == 'agregar':
        if request.method =='POST':
            form = FormTipoAccidente(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/uri/tipoAccidente/todos')

    #EDITAR TIPO DE ACCIDENTE      
    if accion == 'editar':
        if request.method == 'POST':
            form = FormTipoAccidente(request.POST)
            if form.is_valid():
                id_m =  request.POST["id"]
                tipo_accidente_m = form.cleaned_data['tipo_accidente']
                
                try:
                    tipoA = TipoAccidente.objects.get(id=id_m)
                except TipoAccidente.DoesNotExist:
                    raise ValueError("el registro no existe.")
                    
                tipoA.tipo_accidente = tipo_accidente_m
                tipoA.save()
        else:
             
             form = FormTipoAccidente()
            
    
    context = {
        "tipo_accidentes": tipo_accidentes,
        "form": form
    }

    return render(request, "mantenimientosUri/tipoAccidente.html", context)


def obtener_datos_tipo_accidente_edicion(request, tipoA_id):
    try:
        tipo_accidente = TipoAccidente.objects.get(id=tipoA_id)
        data = {
            'id': tipo_accidente.id,
            'tipo_accidente': tipo_accidente.tipo_accidente,
            # Agrega más campos según sea necesario
        }
        return JsonResponse(data)
    except TipoAccidente.DoesNotExist:
        return JsonResponse({'error': 'Registro no encontrado'}, status=404)
    
    #VISTAS DE VIAJABA  COMO 

def mantViajaba(request, accion):

    viajabas = Viajaba.objects.all()
    
    if accion == 'todos':
        form = FormViajaba()

    #   AGREGAR VIAJABA 
    if accion == 'agregar':
        if request.method =='POST':
            form = FormViajaba(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/uri/viajaba/todos')
    
    context = {
        "viajabas": viajabas,
        "form": form
    }

    return render(request, "mantenimientosUri/viajaba.html", context)

    #MANTENIMIENTOS DE COLOR DE PIEL 
def mantColorPiel(request, accion):

    color_piel = ColorPiel.objects.all()
    
    if accion == 'todos':
        form = FormColorPiel()

    #   AGREGAR COLOR DE PIEL  
    if accion == 'agregar':
        if request.method =='POST':
            form = FormColorPiel(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/uri/colorPiel/todos')
    
    context = {
        "color_piel": color_piel,
        "form": form
    }

    return render(request, "mantenimientosUri/colorPiel.html", context)


        #VISTAS DE TEMPERATURA  DE PIEL 
def mantTemperaturaPiel(request, accion):

    temperatura_piel = TemperaturaPiel.objects.all()
    
    if accion == 'todos':
        form = FormTemperaturaPiel()

    #   AGREGAR TEMPERATURA DE PIEL 
    if accion == 'agregar':
        if request.method =='POST':
            form = FormTemperaturaPiel(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/uri/temperaturaPiel/todos')
    
    context = {
        "temperatura_piel": temperatura_piel,
        "form": form
    }

    return render(request, "mantenimientosUri/temperaturaPiel.html", context)

    #VISTAS DE HUMEDAD DE LA PIEL 
def mantHumedadPiel(request, accion):

    humedad_piel = HumedadPiel.objects.all()
    
    if accion == 'todos':
        form = FormHumedadPiel()

    #   AGREGAR HUMEDAD  
    if accion == 'agregar':
        if request.method =='POST':
            form = FormHumedadPiel(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/uri/humedadPiel/todos')
    
    context = {
        "humedad_piel": humedad_piel,
        "form": form
    }

    return render(request, "mantenimientosUri/humedadPiel.html", context)


    #VISTAS DE EVALUACION 
def mantEvaluacion(request, accion):

    evaluacion = Evaluacion.objects.all()
    
    if accion == 'todos':
        form = FormEvaluacion()

    #   AGREGAR EVALUACION
    if accion == 'agregar':
        if request.method =='POST':
            form = FormEvaluacion(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/uri/evaluacion/todos')

    #EDITAR EVALUACION      
    if accion == 'editar':
        if request.method == 'POST':
            form = FormEvaluacion(request.POST)
            if form.is_valid():
                id_m =  request.POST["id"]
                evaluacion_m = form.cleaned_data['evaluacion']
                
                try:
                    evaluaciones = Evaluacion.objects.get(id=id_m)
                except Evaluacion.DoesNotExist:
                    raise ValueError("Evaluación no existe.")
                    
                evaluaciones.servicio = evaluacion_m
                evaluaciones.save()
        else:
             
             form = FormEvaluacion()
            
    
    context = {
        "evaluacion": evaluacion,
        "form": form
    }

    return render(request, "mantenimientosUri/evaluacion.html", context)


def obtener_datos_evaluacion_edicion(request, evaluacion_id):
    try:
        evaluacion = Evaluacion.objects.get(id=evaluacion_id)
        data = {
            'id': evaluacion.id,
            'evaluacion': evaluacion.evaluacion,
            # Agrega más campos según sea necesario
        }
        return JsonResponse(data)
    except Evaluacion.DoesNotExist:
        return JsonResponse({'error': 'Registro no encontrado'}, status=404)
    

    #VISTAS DE INTERVENCION 
def mantIntervencion(request, accion):

    intervencion = Intervenciones.objects.all()
    
    if accion == 'todos':
        form = FormIntervencion()

    #   AGREGAR INTERVENCION
    if accion == 'agregar':
        if request.method =='POST':
            form = FormIntervencion(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/uri/intervencion/todos')

    #EDITAR INTERVENCION    
    if accion == 'editar':
        if request.method == 'POST':
            form = FormIntervencion(request.POST)
            if form.is_valid():
                id_m =  request.POST["id"]
                intervencion_m = form.cleaned_data['intervencion']
                
                try:
                    intervenciones = Intervenciones.objects.get(id=id_m)
                except intervenciones.DoesNotExist:
                    raise ValueError("Evaluación no existe.")
                    
                intervenciones.intervencion = intervencion_m
                intervenciones.save()
        else:
             
             form = FormIntervencion()
            
    
    context = {
        "intervencion": intervencion,
        "form": form
    }

    return render(request, "mantenimientosUri/intervenciones.html", context)


def obtener_datos_intervencion_edicion(request, intervencion_id):
    try:
        intervencion = Intervenciones.objects.get(id=intervencion_id)
        data = {
            'id': intervencion.id,
            'intervencion': intervencion.intervencion,
            # Agrega más campos según sea necesario
        }
        return JsonResponse(data)
    except Intervenciones.DoesNotExist:
        return JsonResponse({'error': 'Registro no encontrado'}, status=404)
        
def DiasSemana():
    dias = DiaSemana.objects.all()
    return dias

def GeneroPaciente():
    generos = Sexo.objects.all()
    return generos

def consulPaciente():
    consultas = ContactoPaciente.objects.all()
    return consultas

def noContactoPaciente():
    noContacto = NoContactoPaciente.objects.all()
    return noContacto

def GeneroAcompanante():
    generosA = Sexo.objects.all()
    return generosA

def EstadosEvento():
    estado = Estados.objects.all()
    return estado

def MunicipiosEvento():
    municipios = Municipios.objects.all()
    return municipios

def ParroquiasEvento():
    parroquias = Parroquias.objects.all()
    return parroquias

def lugarAtencion():
    lugares = Lugares.objects.all()
    return lugares

def ModoTraslado():
    traslados = Traslado.objects.all()
    return traslados

def ViaReporte():
    reportes = Reportes.objects.all()
    return reportes

def TipoServicio():
    servicios = Servicios.objects.all()
    return servicios

def TipoAccidentes():
    accidentes = TipoAccidente.objects.all()
    return accidentes

def TipoArma():
    armas = Tipo_arma.objects.all()
    return armas

def traumaVehiculo():
    vehiculos = TraumaVehiculo.objects.all()
    return vehiculos

def Viajabas():
    viabajas = Viajaba.objects.all()
    return viabajas

def TrumanoIntencional():
    traumas = TraumaNoIntencional.objects.all()
    return traumas

def emergenciasMedicasNoTraumaticas():
    emergencias = EmergenciaNoTraumaticas.objects.all()
    return emergencias

def EvaluacionViaAerea():
    evaluaciones = Evaluacion.objects.all()
    return evaluaciones

def IntervencionViaAerea():
    intervenciones = Intervenciones.objects.all()
    return intervenciones

def ResultadoViaAerea():
    resultados = Resultados.objects.all()
    return resultados

def evaluacionRespiracion():
    evaluacionesRepiracion = EvaluacionRespiracion.objects.all()
    return evaluacionesRepiracion

def intervencionRespiracion():
    intervenciones = IntervencionRespiracion.objects.all()
    return intervenciones

def resultadoRespiracion():
    resultados = ResultadiRespiracion.objects.all()
    return resultados

def colorPiel():
    colores = ColorPiel.objects.all()
    return colores

def temperaturaPiel():
    temperaturas = TemperaturaPiel.objects.all()
    return temperaturas

def humedadPiel():
    humedades = HumedadPiel.objects.all()
    return humedades

def maniobrasPelvis():
    maniobras = ManiobraPelvis.objects.all()
    return maniobras

def reaccionPupilar():
    reacciones = ReaccionPupilar.objects.all()
    return reacciones

def opcionHipotermiar():
    opciones = HipotermiaOpcion.objects.all()
    return opciones
