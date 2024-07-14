from django.urls import path
from .import views

urlpatterns = [
    path('organizacion', views.organizacion, name="organizacion"),
    path('organizacion/reglamentos', views.reglamentos, name="reglamentos"),
    path('organizacion/reglamentos<str:accion>', views.reglamentos_consultar, name="reglamentos_consultar"),
    path('organizacion/reglamentos/update/<int:id>', views.update_reglamentos, name="update_reglamentos"),
    path('organizacion/reglamentos/updatef/<int:id>', views.update_reglamentosf, name="update_reglamentosf"),
    path('organizacion/reglamentos/delete/<int:id>', views.del_reglamentos, name="del_reglamentos"),
    path('organizacion/reglamentos/pubublicar_reg/<int:id>', views.pubublicar_reglamento, name="pubublicar_reglamento"),
    path('organizacion/reglamentos/despubublicar_reg/<int:id>', views.despubublicar_reglamento, name="despubublicar_reglamento"),
    path('organizacion/normativas', views.normativas, name="normativas"),
    path('organizacion/normativas/<str:accion>', views.normativas_consultar, name="normativas_consultar"),
    path('organizacion/normativas/update/<int:id>', views.update_normativas, name="update_normativas"),
    path('organizacion/normativas/updatef/<int:id>', views.updatef_normativas, name="updatef_normativas"),
    path('organizacion/normativas/delete/<int:id>', views.del_normativas, name="del_normativas"),
    path('organizacion/normativas/pubublicar_reg/<int:id>', views.pubublicar_normativas, name="pubublicar_normativas"),
    path('organizacion/normativas/despubublicar_reg/<int:id>', views.despubublicar_normativas, name="despubublicar_normativas"),
]