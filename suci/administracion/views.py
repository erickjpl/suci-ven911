from django.shortcuts import render, redirect, HttpResponse
from .forms import BienesForm, BienesEForm, ConsumibleForm, ConsumibleEForm, MobiliarioForm, MobiliarioEForm, AveriaForm, AveriaEForm, ComprasForm, AsignacionForm, AsignacionEForm
from .models import Bienes, Consumible, Mobiliario, Averia, Compras, Asignacion
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.loader import get_template
from index.decorators import no_autenticado, allowed_users
from django.contrib.auth.decorators import login_required

# VISTAS DE ADMINISTRACION
@login_required(login_url='login')
@allowed_users(allowed_roles=['superusuario'])
def administracion(request):
    return render(request, "administracion.html")

# VISTAS DE BIENES
@login_required(login_url='login')
@allowed_users(allowed_roles=['usuario_solo_vista', 'superusuario'])
def adminbienes(request):
    if request.method == 'POST':
        form21 = BienesForm(request.POST, request.FILES)
        if form21.is_valid():
            form21.save()
            return redirect("/administracion/adminbienes#success")
        else:
            context = {'form21': form21}
            return render(request, 'administracion/adminbienes.html', context)
    bieness = Bienes.objects.all()
    paginator = Paginator(bieness, 15) # 14 objetos por página
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
    context = {'form21': BienesForm(), 'formadmin': BienesEForm(), 'bieness': pagina_actual}
    return render(request, 'adminbienes.html', context)

# VISTAS DE ACTUALIZACIÓN DE BIENES
@login_required(login_url='login')
@allowed_users(allowed_roles=['superusuario'])
def update_bienes(request, id):
    queryset = Bienes.objects.get(id=id)
    form = BienesEForm(instance=queryset)
    if request.method == 'POST':
        form = BienesEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/administracion/adminbienes#updatesuccess')

# VISTAS DE ELIMINACIÓN DE BIENES
@login_required(login_url='login')
@allowed_users(allowed_roles=['superusuario'])
def del_bienes(request, id):
    if request.method == 'POST':
        form = Bienes.objects.get(id=id)
        form.delete()
        return redirect('/administracion/adminbienes#deletesuccess')
    
# VISTAS DE NORMATIVAS - CONSULTAR
@login_required(login_url='login')
@allowed_users(allowed_roles=['usuario_solo_vista', 'superusuario'])
def bienes_consultar(request, accion):
    if accion == 'consultar':
        if 'name' in request.GET:
            ubicacion = request.GET['name']
            bieness = Bienes.objects.filter(estado__contains=ubicacion).values()
            paginator = Paginator(bieness, 15) # 15 objetos por página
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
    context = {'form21': BienesForm(), 'formadmin': BienesEForm(), 'bieness': pagina_actual}
    return render(request, 'adminbienes.html', context)