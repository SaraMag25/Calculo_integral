from django.test import TestCase
from .views import soma_riemann, ajeita_funcao
import math

class IntegralTestCase(TestCase):
    
    def test_integral_constante(self):
        resultado = soma_riemann("5", 0, 2, 1000)
        self.assertAlmostEqual(resultado, 10, places=1)
    
    def test_integral_linear(self):
        resultado = soma_riemann("x", 0, 2, 1000)
        self.assertAlmostEqual(resultado, 2, places=1)
    
    def test_integral_quadratica(self):
        resultado = soma_riemann("x**2", 0, 1, 1000)
        self.assertAlmostEqual(resultado, 1/3, places=2)
    
    def test_integral_seno(self):
        resultado = soma_riemann("sin(x)", 0, math.pi, 2000)
        self.assertAlmostEqual(resultado, 2, places=1)
    
    def test_avaliacao_funcao(self):
        self.assertEqual(ajeita_funcao("x**2", 2), 4)
        self.assertEqual(ajeita_funcao("2*x + 1", 3), 7)
    
    def test_funcoes_trigonometricas(self):
        self.assertAlmostEqual(ajeita_funcao("sin(x)", math.pi/2), 1, places=5)
        self.assertAlmostEqual(ajeita_funcao("cos(x)", 0), 1, places=5)
    
    def test_funcoes_exponenciais(self):
        self.assertAlmostEqual(ajeita_funcao("exp(x)", 0), 1, places=5)
        self.assertAlmostEqual(ajeita_funcao("ln(x)", 1), 0, places=5)