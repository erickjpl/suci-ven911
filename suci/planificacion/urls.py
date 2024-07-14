from django.urls import path
from  .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('inicio/', views.planificacion_inicio, name="planificacion_inicio"),
    path('objetivos', views.objetivos, name="objetivos"),
    path('objetivos<str:accion>', views.objetivos_consultar, name="objetivos_consultar"),
    path('objetivos/update/<int:id>', views.update_objetivos, name="update_objetivos"),
    path('objetivos/delete/<int:id>', views.del_objetivos, name="del_objetivos"),
    path('actividades', views.actividades, name="actividades"),
    path('actividades<str:accion>', views.actividades_consultar, name="actividades_consultar"),
    path('actividades/update/<int:id>', views.update_actividades, name="update_actividades"),
    path('actividades/delete/<int:id>', views.del_actividades, name="del_actividades"),
    path('llamadas', views.llamadas, name="llamadas"),
    path('llamadas/update/<int:id>', views.update_llamadas, name="update_llamadas"),
    path('llamadas/delete/<int:id>', views.del_llamadas, name="del_llamadas"),
    path('llamadas<str:accion>', views.llamadas_consultar, name="llamadas_consultar"),
    path('infraestructura/', views.infraestructura, name="infraestructura"),
    path('infraestructura<str:accion>', views.infraestructura_consultar, name="infraestructura_consultar"),
    path('infraestructura/update/<int:id>', views.update_infraestructura, name="update_infraestructura"),
    path('infraestructura/delete/<int:id>', views.del_infraestructura, name="del_infraestructura"),
    path('metas/', views.metas, name="metas")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)