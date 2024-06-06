from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .controllers.EquipamentController import ListEquipament

urlpatterns = [
    # BEGING Equipament
    path(
        "",
        ListEquipament.as_view(),
        name="listing-equipament",
    ),
    path(
        "<str:filter>",
        ListEquipament.as_view(),
        name="filter-equipament",
    ),
    # END Equipament
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
