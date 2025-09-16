from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calcular/', views.calcular_integral, name='calcular_integral'),
    path('visualizar/', views.visualizar_integral, name='visualizar_integral'),
]
