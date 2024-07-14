from django.shortcuts import render, redirect
from .forms import IncidenciasForm, IncidenciasEForm
from .models import Incidencias

# Create your views here.

def potencia(request):
    if request.method == 'POST':
        formpi = IncidenciasForm(request.POST)
        if formpi.is_valid():
            formpi.save()
        else:
            context = {'formpi': formpi}
            return render(request, 'potencia.html', context)
    incidenciass = Incidencias.objects.all()
    context = {'formpi': IncidenciasForm(), 'formegh': IncidenciasEForm(), 'incidenciass': incidenciass}
    return render(request, 'potencia.html', context)

# VISTAS DE ACTUALIZACIÓN DE POTENCIA
def update_potencia(request, id):
    queryset = Incidencias.objects.get(id=id)
    form = IncidenciasEForm(instance=queryset)
    if request.method == 'POST':
        form = IncidenciasEForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/potencia#updatesuccess')

# VISTAS DE ELIMINACIÓN DE POTENCIA
def del_potencia(request, id):
    if request.method == 'POST':
        form = Incidencias.objects.get(id=id)
        form.delete()
        return redirect('/potencia#deletesuccess')
