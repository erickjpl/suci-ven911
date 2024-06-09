from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .controllers.accounts.CreateSocialMediaAccountController import CreateSocialMediaAccount
from .controllers.accounts.ListSocialMediaAccountController import ListSocialMediaAccount
from .controllers.accounts.SocialMediaAccountController import DeleteSocialMediaAccount, ReadSocialMediaAccount
from .controllers.accounts.UpdateSocialMediaAccountController import UpdateSocialMediaAccount

urlpatterns = [
    path(
        "account",
        ListSocialMediaAccount.as_view(),
        name="listing-account",
    ),
    path(
        "account/crear",
        CreateSocialMediaAccount.as_view(),
        name="create-account",
    ),
    path(
        "account/<int:pk>",
        ReadSocialMediaAccount.as_view(),
        name="gc-reader-social-media-account",
    ),
    path(
        "account/<int:pk>/actualizar",
        UpdateSocialMediaAccount.as_view(),
        name="updater-account",
    ),
    path(
        "account/<int:pk>/eliminar",
        DeleteSocialMediaAccount.as_view(),
        name="destroyer-account",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
