from index.modules.ModuleCardController import ModuleCard

from django.urls import path

urlpatterns = [
    path(
        "",
        ModuleCard.as_view(),
        name="modulos",
    ),
]
