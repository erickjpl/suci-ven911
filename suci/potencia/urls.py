from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('potencia/', views.potencia, name="potencia"),
    path('potencia/update/<int:id>', views.update_potencia, name="update_potencia"),
    path('potencia/delete/<int:id>', views.del_potencia, name="update_potencia"),
]