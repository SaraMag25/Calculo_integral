from django.test import TestCase
from .views import soma_rieamann, ajeita_funcao
import math

class IntegralTestCase(TestCase):
    def test_integral_constante(self):
        #Teste: ∫5 dx de 0 a 2 = 10
        resultado = soma_rieamann("5", 0, 2, 1000)
        self.assertAlmostEqual(resultado, 10, places=1)

    def test_integral_linear(self):
        #Teste: ∫x dx de 0 a 2 = 2
        resultado = soma_rieamann("x", 0, 2, 1000)
        self.assertAlmostEqual(resultado, 2, places=1)
    
    def test_integral_quadratica(self):
        #Teste: ∫x² dx de 0 a 1 = 1/3
        resultado = soma_rieamann("x**2", 0, 1, 1000)
        self.assertAlmostEqual(resultado, 1/3, places=2)
    
    def test_integral_seno(self):
        #Teste: ∫sen(x) dx de 0 a π = 2
        resultado = soma_rieamann("sen(x)", 0, math.pi, 1000)
        self.assertAlmostEqual(resultado, 2, places=1)
    
    