from django.urls import path
from . import views

app_name = 'calculo_integral'

urlpatterns = [
    path('', views.home, name='home'),
    path('calcular/', views.calcular_integral, name='calcular'),
]