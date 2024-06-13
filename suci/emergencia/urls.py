from emergencia.controllers.CreateEmergencyController import CreateEmergency
from emergencia.controllers.DeleteEmergencyController import DeleteEmergency
from emergencia.controllers.ListEmergencyController import ListEmergency
from emergencia.controllers.UpdateEmergencyController import UpdateController

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path("", ListEmergency.as_view(), name="list-emergency"),
    path("create", CreateEmergency.as_view(), name="create-emergency"),
    path("<int:pk>/actualizar", UpdateController.as_view(), name="update-emergency"),
    path("<int:pk>/eliminar", DeleteEmergency.as_view(), name="delete-emergency"),
    # path("completed", views.completed_emergency, name="completed_emergency"),
    # path("search", views.SearchEmergency.as_view(), name="search_emergency"),
    # path("statistics/estado", views.statistics_estado, name="statistics_estado"),
    # path("statistics/municipio", views.statistics_municipio, name="statistics_municipio"),
    # path("statistics/parroquia", views.statistics_parroquia, name="statistics_parroquia"),
    # path("statistics/incidencia", views.statistics_incidencia, name="statistics_incidencia"),
    # path("statistics/organismo", views.statistics_organismo, name="statistics_organismo"),
    # path("<int:emergency_id>", views.update_emergency, name="update_emergency"),
    # path("<int:emergency_id>/complete", views.complete_emergency, name="complete_emergency"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
