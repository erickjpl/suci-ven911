"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from emergency import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('emergency/', views.emergency, name='emergency'),
    path('emergency/completed/', views.completed_emergency, name='completed_emergency'),
    path('emergency/statistics/estado', views.statistics_estado, name='statistics_estado'),
    path('emergency/statistics/municipio', views.statistics_municipio, name='statistics_municipio'),
    path('emergency/statistics/parroquia', views.statistics_parroquia, name='statistics_parroquia'),
    path('emergency/statistics/incidencia', views.statistics_incidencia, name='statistics_incidencia'),
    path('emergency/statistics/organismo', views.statistics_organismo, name='statistics_organismo'),
    path('emergency/create/', views.create_emergency, name='create_emergency'),
    path('emergency/<int:emergency_id>/', views.update_emergency, name='update_emergency'),
    path('emergency/<int:emergency_id>/complete', views.complete_emergency, name='complete_emergency'),
    path('emergency/<int:emergency_id>/delete', views.delete_emergency, name='delete_emergency'),
    path('emergency/search', views.SearchEmergency.as_view(), name='search_emergency'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin')
]
