from django.urls import include, path

urlpatterns = [
    path("auth/", include(("users.authentication.urls", "auth"))),
]
