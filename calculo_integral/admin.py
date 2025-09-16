from django.contrib import admin
from .models import CalculandoIntegrais

@admin.register(CalculandoIntegrais)
class CalculoIntegralAdmin(admin.ModelAdmin):
    list_display = ['funcao', 'limite_inferior', 'limite_superior', 'resultado', 'data_calculo']
    list_filter = ['data_calculo']
    search_fields = ['funcao']
    readonly_fields = ['data_calculo']