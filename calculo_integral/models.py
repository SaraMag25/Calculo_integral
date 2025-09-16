from django.db import models

class CalculandoIntegrais(models.Model):
    funcao = models.CharField(max_length=200, verbose_name="Função")
    limite_inferior = models.FloatField(verbose_name="Limite Inferior")
    limite_superior = models.FloatField(verbose_name="Limite Superior")
    resultado = models.FloatField(verbose_name="Resultado")
    numero_retangulos = models.IntegerField(verbose_name="Número de Retângulos")
    erro_estimado = models.FloatField(verbose_name="Erro Estimado")
    data_calculo = models.DateTimeField(auto_now_add=True, verbose_name="Data do Cálculo")

    def __str__(self):
        return f"∫{self.funcao} de {self.limite_inferior} a {self.limite_superior}"

    class Meta:
        verbose_name = "Cálculo de Integral"
        verbose_name_plural = "Cálculos de Integrais"