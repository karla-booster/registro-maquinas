from django.urls import path
from . import views

urlpatterns = [
    path('maquinas/', views.list, name="lista-maquinas"),
    path('area/<int:area_id>/', views.area, name="areas"),
    path('maquina/<int:maquina_id>/', views.maquina, name="maquinas")
]