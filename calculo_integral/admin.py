from django.contrib import admin
from .models import CalculoIntegral

@admin.register(CalculoIntegral)
class CalculoIntegralAdmin(admin.ModelAdmin):
    list_display = ['funcao', 'limite_inferior', 'limite_superior', 'resultado', 'data_calculo']
    list_filter = ['data_calculo']
