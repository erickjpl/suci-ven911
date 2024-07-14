from django.urls import path
from  .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('biblioteca/', views.biblioteca, name="biblioteca"),
    path('biblioteca_normativas/', views.biblioteca_normativas, name="biblioteca_normativas"),
    path('biblioteca_normativas/<str:accion>', views.biblioteca_normativas_consultar, name="biblioteca_normativas_consultar"),
    path('biblioteca_reglamentos/', views.biblioteca_reglamentos, name="biblioteca_reglamentos"),
    path('biblioteca_reglamentos/<str:accion>', views.biblioteca_reglamentos_consultar, name="biblioteca_reglamentos_consultar"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
