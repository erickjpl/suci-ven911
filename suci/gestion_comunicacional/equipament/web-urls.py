from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .controllers.EquipamentController import (
    CreateEquipament,
    DeleteEquipament,
    EquipamentView,
    ListEquipament,
    ReadEquipament,
    UpdateEquipament,
)
from .controllers.EquipamentLoanController import (
    CreateEquipamentLoan,
    DeleteEquipamentLoan,
    ListEquipamentLoan,
    ReadEquipamentLoan,
    UpdateEquipamentLoan,
)

urlpatterns = [
    # BEGING Equipament
    path(
        "",
        EquipamentView.as_view(template_name="gc/equipament/listing-equipaments.html"),
        name="listing-equipament",
    ),
    path(
        "filter<str:filter>",
        EquipamentView.as_view(template_name="gc/equipament/listing-equipaments.html"),
        name="filter-equipament",
    ),
    path(
        "actualizar/<int:pk>",
        EquipamentView.as_view(template_name="gc/equipament/listing-equipaments.html"),
        name="updater-equipament",
    ),
    # END Equipament
    path(
        "crear",
        CreateEquipament.as_view(),
        name="create-equipament",
    ),
    path(
        "detalle/<int:pk>",
        ReadEquipament.as_view(),
        name="reader-equipament",
    ),
    path(
        "eliminar/<int:pk>",
        DeleteEquipament.as_view(),
        name="destroyer-equipament",
    ),
    path(
        "loan",
        ListEquipamentLoan.as_view(),
        name="listing-loan",
    ),
    path(
        "loan/<str:accion>",
        ListEquipamentLoan.as_view(),
        name="filter-loan",
    ),
    path(
        "loan/crear",
        CreateEquipamentLoan.as_view(),
        name="create-loan",
    ),
    path(
        "loan/detalle/<int:pk>",
        ReadEquipamentLoan.as_view(),
        name="reader-loan",
    ),
    path(
        "loan/actualizar/<int:pk>",
        UpdateEquipamentLoan.as_view(),
        name="updater-loan",
    ),
    path(
        "loan/eliminar/<int:pk>",
        DeleteEquipamentLoan.as_view(),
        name="destroyer-loan",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
