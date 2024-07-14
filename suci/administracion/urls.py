from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('administracion', views.administracion, name="administracion"),
    path('adminbienes', views.adminbienes, name="adminbienes"),
    path('bienes<str:accion>', views.bienes_consultar, name="bienes_consultar"),
    path('bienes/update/<int:id>', views.update_bienes, name="update_bienes"),
    path('bienes/delete/<int:id>', views.del_bienes, name="del_bienes"),
    #path('compras', views.compras, name="compras"),
    #path('consumible', views.consumible, name="consumible"),
    #path('vehiculos', views.vehiculos, name="vehiculos"),
]