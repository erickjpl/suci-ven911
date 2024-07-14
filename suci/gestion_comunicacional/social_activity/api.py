from gestion_comunicacional.social_activity.controllers.CreateSocialActivityController import CreateSocialActivityApi
from gestion_comunicacional.social_activity.controllers.DeleteSocialActivityController import DeleteSocialActivityApi
from gestion_comunicacional.social_activity.controllers.ListSocialActivityController import ListSocialActivityApi
from gestion_comunicacional.social_activity.controllers.UpdateSocialActivityController import UpdaterSocialActivityApi

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path(
        "",
        ListSocialActivityApi.as_view(),
        name="list-activity",
    ),
    path(
        "crear",
        CreateSocialActivityApi.as_view(),
        name="create-activity",
    ),
    path(
        "<int:pk>/actualizar",
        UpdaterSocialActivityApi.as_view(),
        name="update-activity",
    ),
    path(
        "<int:pk>/eliminar",
        DeleteSocialActivityApi.as_view(),
        name="delete-activity",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
