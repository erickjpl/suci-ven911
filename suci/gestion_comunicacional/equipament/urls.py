from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .controllers.EquipamentController import (
    CreateEquipament,
    DeleteEquipament,
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
    path(
        "",
        ListEquipament.as_view(),
        name="listing-equipament",
    ),
    path(
        "<str:accion>",
        ListEquipament.as_view(),
        name="filter-equipament",
    ),
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
        "actualizar/<int:pk>",
        UpdateEquipament.as_view(),
        name="updater-equipament",
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
