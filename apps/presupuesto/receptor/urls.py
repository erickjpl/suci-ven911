from django.urls import path

from .views.create_view import ReceptorCreateView
from .views.delete_view import ReceptorDeleteView
from .views.list_view import ReceptorListView
from .views.update_view import ReceptorUpdateView

urlpatterns = [
    path(
        "",
        ReceptorListView.as_view(),
        name="list",
    ),
    path(
        "create",
        ReceptorCreateView.as_view(),
        name="create",
    ),
    path(
        "<int:pk>/read",
        ReceptorListView.as_view(),
        name="read",
    ),
    path(
        "<int:pk>/update",
        ReceptorUpdateView.as_view(),
        name="update",
    ),
    path(
        "<int:pk>/delete",
        ReceptorDeleteView.as_view(),
        name="delete",
    ),
]