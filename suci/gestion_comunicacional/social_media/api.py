from gestion_comunicacional.social_media.controllers.accounts.CreateSocialMediaAccountController import CreateSocialMediaAccountApi
from gestion_comunicacional.social_media.controllers.accounts.DeleteSocialMediaAccountController import DeleteSocialMediaAccountApi
from gestion_comunicacional.social_media.controllers.accounts.ListSocialMediaAccountController import ListSocialMediaAccountApi
from gestion_comunicacional.social_media.controllers.accounts.UpdateSocialMediaAccountController import UpdateSocialMediaAccountApi

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path(
        "account",
        ListSocialMediaAccountApi.as_view(),
        name="list-account",
    ),
    path(
        "account/crear",
        CreateSocialMediaAccountApi.as_view(),
        name="create-account",
    ),
    path(
        "account/<int:pk>/actualizar",
        UpdateSocialMediaAccountApi.as_view(),
        name="update-account",
    ),
    path(
        "account/<int:pk>/eliminar",
        DeleteSocialMediaAccountApi.as_view(),
        name="delete-account",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
