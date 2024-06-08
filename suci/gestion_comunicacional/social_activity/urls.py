from gestion_comunicacional.social_activity.controllers.CreateSocialActivityController import CreateSocialActivity
from gestion_comunicacional.social_activity.controllers.ListSocialActivityController import ListSocialActivity
from gestion_comunicacional.social_activity.controllers.SocialActivityController import (
    DeleteSocialActivity,
    ReadSocialActivity,
    UpdateSocialActivity,
)

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path(
        "",
        ListSocialActivity.as_view(),
        name="listing-activity",
    ),
    path(
        "crear",
        CreateSocialActivity.as_view(),
        name="create-activity",
    ),
    path(
        "<int:pk>",
        ReadSocialActivity.as_view(),
        name="reader-activity",
    ),
    path(
        "<int:pk>/actualizar",
        UpdateSocialActivity.as_view(),
        name="updater-activity",
    ),
    path(
        "<int:pk>/eliminar",
        DeleteSocialActivity.as_view(),
        name="destroyer-activity",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
