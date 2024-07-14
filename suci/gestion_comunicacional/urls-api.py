from gestion_comunicacional.info.InfoController import InfoControllerApi

from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("", InfoControllerApi.as_view(), name="info"),
    path("social-media/", include(("gestion_comunicacional.social_media.api", "sm"))),
    path(
        "social-activity/",
        include(("gestion_comunicacional.social_activity.api", "sa")),
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
