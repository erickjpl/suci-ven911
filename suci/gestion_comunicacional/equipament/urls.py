from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# Equipament Loan
from .controllers.EquipamentLoanController import (
    CreateEquipamentLoan,
    DeleteEquipamentLoan,
    ListEquipamentLoan,
    ReadEquipamentLoan,
    UpdateEquipamentLoan,
)

# Equipament
from .controllers.equipaments.CreateEquipamentController import CreateEquipament
from .controllers.equipaments.DeleteEquipamentController import DeleteEquipament
from .controllers.equipaments.ListEquipamentController import ListEquipament
from .controllers.equipaments.ReadEquipamentController import ReadEquipament
from .controllers.equipaments.UpdateEquipamentController import UpdateEquipament

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
        UpdateEquipament.as_view(template_name="gc/equipament/listing.html"),
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
