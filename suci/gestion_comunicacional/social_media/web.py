from gestion_comunicacional.social_media.controllers.accounts.CreateSocialMediaAccountController import CreateSocialMediaAccount
from gestion_comunicacional.social_media.controllers.accounts.DeleteSocialMediaAccountController import DeleteSocialMediaAccount
from gestion_comunicacional.social_media.controllers.accounts.ListSocialMediaAccountController import ListSocialMediaAccount
from gestion_comunicacional.social_media.controllers.accounts.UpdateSocialMediaAccountController import UpdateSocialMediaAccount

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path(
        "account",
        ListSocialMediaAccount.as_view(),
        name="list-account",
    ),
    path(
        "account/crear",
        CreateSocialMediaAccount.as_view(),
        name="create-account",
    ),
    path(
        "account/<int:pk>/actualizar",
        UpdateSocialMediaAccount.as_view(),
        name="update-account",
    ),
    path(
        "account/<int:pk>/eliminar",
        DeleteSocialMediaAccount.as_view(),
        name="delete-account",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)