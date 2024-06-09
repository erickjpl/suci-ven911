# Equipament
# Equipament Loan
from gestion_comunicacional.equipament.controllers.EquipamentLoanController import (
    CreateEquipamentLoan,
    DeleteEquipamentLoan,
    ListEquipamentLoan,
    ReadEquipamentLoan,
    UpdateEquipamentLoan,
)
from gestion_comunicacional.equipament.controllers.equipaments.CreateEquipamentController import CreateEquipament
from gestion_comunicacional.equipament.controllers.equipaments.DeleteEquipamentController import DeleteEquipament
from gestion_comunicacional.equipament.controllers.equipaments.ListEquipamentController import ListEquipament
from gestion_comunicacional.equipament.controllers.equipaments.ReadEquipamentController import ReadEquipament
from gestion_comunicacional.equipament.controllers.equipaments.UpdateEquipamentController import UpdateEquipament

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    # BEGING Equipament
    path(
        "",
        ListEquipament.as_view(),
        name="listing-equipament",
    ),
    path(
        "crear",
        CreateEquipament.as_view(),
        name="create-equipament",
    ),
    path(
        "<int:pk>",
        ReadEquipament.as_view(),
        name="reader-equipament",
    ),
    path(
        "<int:pk>/actualizar",
        UpdateEquipament.as_view(),
        name="updater-equipament",
    ),
    path(
        "<int:pk>/eliminar",
        DeleteEquipament.as_view(),
        name="destroyer-equipament",
    ),
    # BEGING Equipament Loan
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
