from django.db import models

class CalculandoIntegrais(models.Model):
    funcao = models.CharField(max_length=200)
    limite_inferior = models.FloatField()
    limite_superior = models.FloatField()
    resultado = models.FloatField()

    def __str__(self):
        return f"∫{self.funcao} de {self.limite_inferior} a {self.limite_superior}"