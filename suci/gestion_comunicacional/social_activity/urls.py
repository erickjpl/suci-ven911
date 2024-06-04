from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .controllers.SocialActivityController import (
    CreateSocialActivity,
    DeleteSocialActivity,
    ListSocialActivity,
    ReadSocialActivity,
    UpdateSocialActivity,
)

urlpatterns = [
    path(
        "",
        ListSocialActivity.as_view(),
        name="listing-activity",
    ),
    path(
        "<str:accion>",
        ListSocialActivity.as_view(),
        name="filter-activity",
    ),
    path(
        "crear",
        CreateSocialActivity.as_view(),
        name="create-activity",
    ),
    path(
        "detalle/<int:pk>",
        ReadSocialActivity.as_view(),
        name="reader-activity",
    ),
    path(
        "actualizar/<int:pk>",
        UpdateSocialActivity.as_view(),
        name="updater-activity",
    ),
    path(
        "eliminar/<int:pk>",
        DeleteSocialActivity.as_view(),
        name="destroyer-activity",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
