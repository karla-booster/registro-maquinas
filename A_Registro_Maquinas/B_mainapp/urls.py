from django.urls import path
from . import views

urlpatterns = [
    path('', views.estado_general, name="estado-general"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('registro/', views.register_page, name="register"),
    path('login/auto', views.login_qr, name="login_qr"),
]
