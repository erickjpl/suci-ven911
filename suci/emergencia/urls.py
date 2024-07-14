from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

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