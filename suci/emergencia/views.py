from django.shortcuts import render, redirect
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from paneluser.models import Usuarios
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import FileResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from index.decorators import no_autenticado, allowed_users
from .forms import EmergencyForm
from .models import Emergency, Estado, Municipio, Parroquia, Incidencia, OrganismoCompetente
from django.views.generic import ListView
from django.utils import timezone
import json


# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = Usuarios.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('emergency')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })

@login_required 
def emergency(request):
    emergencies = Emergency.objects.filter(user=request.user, datecompleted__isnull=True)
    paginator = Paginator(emergencies, 10)  # Show 20 emergencies per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'emergency.html', {
        'emergencies': paginator.page(page_number),
        'page_obj': page_obj
    })

@login_required
def completed_emergency(request):
    emergencies = Emergency.objects.filter(user=request.user, datecompleted__isnull=False)
    paginator = Paginator(emergencies, 10)  # Show 20 emergencies per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'emergency.html', {
        'emergencies': paginator.page(page_number),
        'page_obj': page_obj
    })

@login_required
def statistics_estado(request):
    labels = []
    data = []

    queryset1 = Estado.objects.order_by('-nombre')
    queryset2 = Emergency.objects.values('id_estado').annotate(my_count=Count('id')).order_by('-id_estado')
    for estado in queryset1:
        labels.append(estado.nombre)

    for emergency in queryset2:
        print(emergency['my_count'])
        data.append(emergency['my_count'])

    return render(request, 'statistics_estado.html', {
        'labels': labels,
        'data': data
    })

@login_required
def statistics_municipio(request):
    labels = []
    data = []

    queryset1 = Municipio.objects.order_by('-nombre')
    queryset2 = Emergency.objects.values('id_municipio').annotate(my_count=Count('id')).order_by('-id_municipio')

    for municipio in queryset1:
        labels.append(municipio.nombre)

    for emergency in queryset2:
        data.append(emergency['my_count'])

    return render(request, 'statistics_municipio.html', {
        'labels': labels,
        'data': data
    })

@login_required
def statistics_parroquia(request):
    labels = []
    data = []

    queryset1 = Parroquia.objects.order_by('-nombre')
    queryset2 = Emergency.objects.values('id_parroquia').annotate(my_count=Count('id')).order_by('-id_parroquia')

    for parroquia in queryset1:
        labels.append(parroquia.nombre)

    for emergency in queryset2:
        data.append(emergency['my_count'])

    return render(request, 'statistics_parroquia.html', {
        'labels': labels,
        'data': data
    })   

@login_required
def statistics_incidencia(request):
    labels = []
    data = []

    queryset1 = Incidencia.objects.order_by('-tipo')
    queryset2 = Emergency.objects.values('id_incidencia').annotate(my_count=Count('id')).order_by()
    for incidencia in queryset1:
        labels.append(incidencia.tipo)

    for emergency in queryset2:
        data.append(emergency['my_count'])

    return render(request, 'statistics_incidencia.html', {
        'labels': labels,
        'data': data
    })

@login_required
def statistics_organismo(request):
    labels = []
    data = []

    queryset1 = OrganismoCompetente.objects.order_by('-nombre')
    queryset2 = Emergency.objects.values('id_organismo').annotate(my_count=Count('id')).order_by('-id_organismo')
    for organismo in queryset1:
        labels.append(organismo.nombre)

    for emergency in queryset2:
        data.append(emergency['my_count'])

    return render(request, 'statistics_organismo.html', {
        'labels': labels,
        'data': data
    })

@login_required
def create_emergency(request):
    if request.method == 'GET':
        return render(request, 'create_emergency.html', {
            'form': EmergencyForm
        })
    else:
        try:
            form = EmergencyForm(request.POST)
            new_emergency = form.save(commit=False)
            new_emergency.user = request.user
            new_emergency.save()
            return redirect('emergency')
        except ValueError:
            return render(request, 'create_emergency.html', {
                'form': EmergencyForm,
                'error': 'Please provide valid data'
            })

@login_required
def update_emergency(request, emergency_id):
    if request.method == 'GET':
        emergency = get_object_or_404(Emergency, pk=emergency_id, user=request.user)
        form = EmergencyForm(instance=emergency)
        return render(request, 'update_emergency.html', {
            'emergency': emergency,
            'form': form
        })
    else:
        try:
            emergency = get_object_or_404(Emergency, pk=emergency_id, user=request.user)
            form = EmergencyForm(request.POST, instance=emergency)
            form.save()
            return redirect('emergency')
        except ValueError:
            return render(request, 'update_emergency.html', {
                'emergency': emergency,
                'form': form,
                'error': 'Error updating emergency'
            })

@login_required
def complete_emergency(request, emergency_id):
    emergency = get_object_or_404(Emergency, pk=emergency_id, user=request.user)
    if request.method == 'POST':
        emergency.datecompleted = timezone.now()
        emergency.save()
        return redirect('emergency')

@login_required
def delete_emergency(request, emergency_id):
    emergency = get_object_or_404(Emergency, pk=emergency_id, user=request.user)
    if request.method == 'POST':
        emergency.delete()
        return redirect('emergency')

class SearchEmergency(ListView):
    model = Emergency
    template_name = 'emergency.html'
    context_object_name = 'emergencies'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Emergency.objects.filter(denunciante__icontains=query, user=self.request.user)

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('emergency')