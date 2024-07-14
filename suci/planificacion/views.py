from django.shortcuts import render, redirect
from .forms import ObjetivosForm, ObjetivosUForm, ActividadesForm, ActividadesUForm, LlamadasForm, LlamadasUForm, InfraestructuraForm, InfraestructuraEForm
from .models import Objetivos, Actividades, Llamadas, Infraestructura
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.loader import get_template
from index.decorators import no_autenticado, allowed_users
from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa

# VISTAS DE PLANIFICACION
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'usuario_solo_vista', 'superusuario'])
def planificacion_inicio(request):
        return render(request, 'iniciopla.html')

# VISTAS DE PLANIFICACION -  OBJETIVOS
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'usuario_solo_vista', 'superusuario'])
def objetivos(request):
    if request.method == 'POST':
        form17 = ObjetivosForm(request.POST)
        if form17.is_valid():
            form17.save()
        else:
            context = {'form17': form17}
            return render(request, 'objetivos.html', context)
    objetivoss = Objetivos.objects.all()
    paginator = Paginator(objetivoss, 15) # 15 objetos por página
    pagina = request.GET.get('page')
    try:
        # Obtener la página solicitada
        pagina_actual = paginator.page(pagina)
    except PageNotAnInteger:
        # Si la página no es un entero, redirigir a la primera página
        pagina_actual = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, redirigir a la última página
        pagina_actual = Paginator.page(paginator.num_pages)    
    context = {'form17': ObjetivosForm(), 'formob': ObjetivosUForm(), 'objetivoss': pagina_actual}
    return render(request, 'objetivos.html', context)

# VISTAS DE PRESUPUESTO - CONSULTAR - PROYECTO
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'usuario_solo_vista', 'superusuario'])
def objetivos_consultar(request, accion):
    if accion == 'consultar':
        if 'nombrep' in request.GET:
            nombrep = request.GET['nombrep']
            proyectoo = Objetivos.objects.filter(nombrep=nombrep)
            paginator = Paginator(proyectoo, 5) # 14 objetos por página
        pagina = request.GET.get('page')
        try:
            # Obtener la página solicitada
            pagina_actual = paginator.page(pagina)
        except PageNotAnInteger:
            # Si la página no es un entero, redirigir a la primera página
            pagina_actual = paginator.page(1)
        except EmptyPage:
            # Si la página está fuera de rango, redirigir a la última página
            pagina_actual = paginator.page(paginator.num_pages)
        context = {'form17': ObjetivosForm(), 'formob': ObjetivosUForm(), 'objetivoss': pagina_actual}
        return render(request, 'objetivos.html', context)

# VISTAS DE ACTUALIZACIÓN DE PRESUPUESTO - PROYECTO
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'superusuario'])
def update_objetivos(request, id):
    queryset = Objetivos.objects.get(id=id)
    form17 = ObjetivosUForm(instance=queryset)
    if request.method == 'POST':
        form17 = ObjetivosUForm(request.POST, instance=queryset)
        if form17.is_valid():
            form17.save()
            return redirect('/planificacion/objetivos#updatesuccess')

# VISTAS DE ELIMINACIÓN DE PRESUPUESTO - PROYECTO
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'superusuario'])
def del_objetivos(request, id):
    if request.method == 'POST':
        form17 = Objetivos.objects.get(id=id)
        form17.delete()
        return redirect('/planificacion/objetivos#deletesuccess')
    
# VISTAS DE PLANIFICACION -  ACTIVIDADES
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'usuario_solo_vista', 'superusuario'])
def actividades(request):
    if request.method == 'POST':
        form18 = ActividadesForm(request.POST)
        if form18.is_valid():
            form18.save()
            return redirect('/planificacion/actividades#updatesuccess')
        else:
            context = {'form18': form18}
            return render(request, 'planificacion/actividades.html', context)
    actividadess = Actividades.objects.all()
    paginator = Paginator(actividadess, 15) # 15 objetos por página
    pagina = request.GET.get('page')
    try:
        # Obtener la página solicitada
        pagina_actual = paginator.page(pagina)
    except PageNotAnInteger:
        # Si la página no es un entero, redirigir a la primera página
        pagina_actual = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, redirigir a la última página
        pagina_actual = Paginator.page(paginator.num_pages)    
    context = {'form18': ActividadesForm(), 'formac': ActividadesUForm(), 'actividadess': pagina_actual}
    return render(request, 'actividades.html', context)

# VISTAS DE PLANIFICACION - CONSULTAR - PROYECTO
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'usuario_solo_vista', 'superusuario'])
def actividades_consultar(request, accion):
    if accion == 'consultar':
        if 'nombrep' in request.GET:
            nombrep = request.GET['nombrep']
            actividadess = Actividades.objects.filter(nombrep=nombrep)
            paginator = Paginator(actividadess, 15) # 14 objetos por página
        pagina = request.GET.get('page')
        try:
            # Obtener la página solicitada
            pagina_actual = paginator.page(pagina)
        except PageNotAnInteger:
            # Si la página no es un entero, redirigir a la primera página
            pagina_actual = paginator.page(1)
        except EmptyPage:
            # Si la página está fuera de rango, redirigir a la última página
            pagina_actual = paginator.page(paginator.num_pages)
        context = {'form18': ActividadesForm(), 'formac': ActividadesUForm(), 'actividadess': pagina_actual}
        return render(request, 'actividades.html', context)
    
# VISTAS DE ACTUALIZACIÓN DE PLANIFICACION - ACTIVIDADES
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'superusuario'])
def update_actividades(request, id):
    queryset = Actividades.objects.get(id=id)
    form18 = ActividadesUForm(instance=queryset)
    if request.method == 'POST':
        form18 = ActividadesUForm(request.POST, instance=queryset)
        if form18.is_valid():
            form18.save()
            return redirect('/planificacion/actividades#updatesuccess')

# VISTAS DE ELIMINACIÓN DE PLANIFICACION - ACTIVIDADES
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'superusuario'])
def del_actividades(request, id):
    if request.method == 'POST':
        form18 = Actividades.objects.get(id=id)
        form18.delete()
        return redirect('/planificacion/actividades#deletesuccess')

# VISTAS DE PLANIFICACION -  LLAMADAS
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'usuario_solo_vista', 'superusuario'])
def llamadas(request):
    if request.method == 'POST':
        form19 = LlamadasForm(request.POST)
        if form19.is_valid():
            form19.save()
        else:
            context = {'form19': form19}
            return render(request, 'llamadas.html', context)
    llamadass = Llamadas.objects.all()
    paginator = Paginator(llamadass, 15) # 15 objetos por página
    pagina = request.GET.get('page')
    try:
        # Obtener la página solicitada
        pagina_actual = paginator.page(pagina)
    except PageNotAnInteger:
        # Si la página no es un entero, redirigir a la primera página
        pagina_actual = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, redirigir a la última página
        pagina_actual = Paginator.page(paginator.num_pages)    
    context = {'form19': LlamadasForm(), 'formlla': LlamadasUForm(), 'llamadass': pagina_actual}
    return render(request, 'llamadas.html', context)

# VISTAS DE PLANIFICACION - CONSULTAR - PROYECTO
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'usuario_solo_vista', 'superusuario'])
def llamadas_consultar(request, accion):
    if accion == 'consultar':
        if 'estado' in request.GET:
            estado = request.GET['estado']
            llamadass = Llamadas.objects.filter(estado=estado)
            paginator = Paginator(llamadass, 15) # 14 objetos por página
        pagina = request.GET.get('page')
        try:
            # Obtener la página solicitada
            pagina_actual = paginator.page(pagina)
        except PageNotAnInteger:
            # Si la página no es un entero, redirigir a la primera página
            pagina_actual = paginator.page(1)
        except EmptyPage:
            # Si la página está fuera de rango, redirigir a la última página
            pagina_actual = paginator.page(paginator.num_pages)
        context = {'form19': LlamadasForm(), 'formlla': LlamadasUForm(), 'llamadass': pagina_actual}
        return render(request, 'llamadas.html', context)

# VISTAS DE ACTUALIZACIÓN DE PLANIFICACION - LLAMADAS
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'superusuario'])
def update_llamadas(request, id):
    queryset = Llamadas.objects.get(id=id)
    form19 = LlamadasUForm(instance=queryset)
    if request.method == 'POST':
        form19 = LlamadasUForm(request.POST, instance=queryset)
        if form19.is_valid():
            form19.save()
            return redirect('/planificacion/llamadas#updatesuccess')

# VISTAS DE ELIMINACIÓN DE PLANIFICACION - LLAMADAS
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'superusuario'])
def del_llamadas(request, id):
    if request.method == 'POST':
        form19 = Llamadas.objects.get(id=id)
        form19.delete()
        return redirect('/planificacion/llamadas#deletesuccess')

# VISTAS DE METAS
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'usuario_solo_vista', 'superusuario'])
def metas(request):
    llamadass = Llamadas.objects.all()
    paginator = Paginator(llamadass, 15) # 15 objetos por página
    pagina = request.GET.get('page')
    try:
        # Obtener la página solicitada
        pagina_actual = paginator.page(pagina)
    except PageNotAnInteger:
        # Si la página no es un entero, redirigir a la primera página
        pagina_actual = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, redirigir a la última página
        pagina_actual = Paginator.page(paginator.num_pages)    
    context = {'llamadass': pagina_actual}
    return render(request, 'metas.html', context)

# VISTAS DE PLANIFICACION -  LLAMADAS
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'usuario_solo_vista', 'superusuario'])
def infraestructura(request):
    if request.method == 'POST':
        form20 = InfraestructuraForm(request.POST)
        if form20.is_valid():
            form20.save()
            return redirect("/planificacion/infraestructura#success")
        else:
            context = {'form20': form20}
            return render(request, 'planificacion/infraestructura.html', context)
    infraestructuraa =  Infraestructura.objects.all()
    paginator = Paginator(infraestructuraa, 15) # 15 objetos por página
    pagina = request.GET.get('page')
    try:
        # Obtener la página solicitada
        pagina_actual = paginator.page(pagina)
    except PageNotAnInteger:
        # Si la página no es un entero, redirigir a la primera página
        pagina_actual = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, redirigir a la última página
        pagina_actual = Paginator.page(paginator.num_pages)    
    context = {'form20': InfraestructuraForm(), 'forminfra': InfraestructuraEForm(), 'infraestructuraa': pagina_actual}
    return render(request, 'infraestructura.html', context)

# VISTAS DE ACTUALIZACIÓN DE PLANIFICACION - INFRAESTRUCTURA
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'superusuario'])
def update_infraestructura(request, id):
    queryset = Infraestructura.objects.get(id=id)
    form20 = InfraestructuraEForm(instance=queryset)
    if request.method == 'POST':
        form20 = InfraestructuraEForm(request.POST, instance=queryset)
        if form20.is_valid():
            form20.save()
            return redirect('/planificacion/infraestructura#updatesuccess')

# VISTAS DE ELIMINACIÓN DE PLANIFICACION - INFRAESTRUCTURA
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'superusuario'])
def del_infraestructura(request, id):
    if request.method == 'POST':
        form20 = Infraestructura.objects.get(id=id)
        form20.delete()
        return redirect('/planificacion/infraestructura#deletesuccess')

# VISTAS DE INFRAESTRUCTURA - CONSULTAR
@login_required(login_url='login')
@allowed_users(allowed_roles=['presu_plani_admin', 'presu_plani_estandar', 'usuario_solo_vista', 'superusuario'])
def infraestructura_consultar(request, accion):
    if accion == 'consultar':
        if 'name' in request.GET:
            estado = request.GET['name']
            infraestructuraa = Infraestructura.objects.filter(estado__contains=estado).values()
            paginator = Paginator(infraestructuraa, 15) # 15 objetos por página
            pagina = request.GET.get('page')
            try:
                # Obtener la página solicitada
                pagina_actual = paginator.page(pagina)
            except PageNotAnInteger:
                # Si la página no es un entero, redirigir a la primera página
                pagina_actual = paginator.page(1)
            except EmptyPage:
                # Si la página está fuera de rango, redirigir a la última página
                pagina_actual = paginator.page(paginator.num_pages)
    context = {'form20': InfraestructuraForm(), 'forminfra': InfraestructuraEForm(), 'infraestructuraa': pagina_actual}
    return render(request, 'infraestructura.html', context)