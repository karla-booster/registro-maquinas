from django.urls import path
from . import views

urlpatterns = [
    path('calidad/control-metrologia/', views.aprobar, name="calidad-aprobar"),
]