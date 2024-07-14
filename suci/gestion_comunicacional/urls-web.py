from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from .info.InfoController import InfoController

urlpatterns = [
    path("", InfoController.as_view(), name="info"),
    path("social-media/", include(("gestion_comunicacional.social_media.web", "sm"))),
    path("social-activity/",include(("gestion_comunicacional.social_activity.web", "sa")),
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
