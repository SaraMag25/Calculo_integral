from django.shortcuts import render
#from django.http import JsonResponse
from .models import CalculandoIntegrais
import math
#import re

def home(request):
    return render(request, 'calculo_integral/home.html') 
def calcular_integral(request):
    if request.method == "POST":
        try:
            funcao = request.POST.get('funcao', '').strip()
            a = float(request.POST.get('limite_inferior'))
            b = float(request.POST.get('limite_superior'))
            tolerancia = float(request.POST.get('tolerancia', 1e-6))

            resultado, n_usado, erro_estimado = calcular_integral_adaptativa(funcao, a, b, tolerancia)
            
            calculo = CalculandoIntegrais.objects.create(
                funcao=funcao,
                limite_inferior=a,
                limite_superior=b,
                resultado=resultado,
                numero_retangulos=n_usado,
                erro_estimado=erro_estimado
            )
            
            context = {
                'resultado': resultado,
                'funcao': funcao,
                'limite_inferior': a,
                'limite_superior': b,
                'numero_retangulos': n_usado,
                'erro_estimado': erro_estimado,
                'tolerancia': tolerancia,
            }
            return render(request, 'calculo_integral/resultado.html', context)
    
        except Exception as e:
            return render(request, 'calculo_integral/home.html', {'erro': str(e)})
    
    return render(request, 'calculo_integral/home.html')

def calcular_integral_adaptativa(funcao_str, a, b, tolerancia):
    n = 100
    max_iter = 20
    resultado_anterior = 0
    
    for i in range(max_iter):
        resultado_atual = soma_riemann(funcao_str, a, b, n)
        
        if i > 0:
            erro = abs(resultado_atual - resultado_anterior)
            if erro < tolerancia:
                return resultado_atual, n, erro
        
        resultado_anterior = resultado_atual
        n *= 2
    
    return resultado_atual, n, abs(resultado_atual - resultado_anterior)

def soma_riemann(funcao_str, a, b, n):
    h = (b - a) / n
    soma = 0
    
    for i in range(n):
        x = a + i * h + h/2  # Ponto médio
        try:
            y = ajeita_funcao(funcao_str, x)
            soma += y * h
        except:
            continue
    
    return soma

def visualizar_integral(request):
    context = {}
    if request.method == "POST":
        funcao = request.POST.get('funcao', 'x**2')
        a = float(request.POST.get('limite_inferior', 0))
        b = float(request.POST.get('limite_superior', 2))
        n = int(request.POST.get('retangulos', 20))
        
        # Calcula apenas o valor da integral
        resultado = soma_riemann(funcao, a, b, n)
        
        context = {
            'funcao': funcao,
            'limite_inferior': a,
            'limite_superior': b,
            'retangulos_num': n,
            'resultado': resultado,
        }
    
    return render(request, 'calculo_integral/visualizacao.html', context)

def ajeita_funcao(funcao_str, x):

    funcao = funcao_str.replace('^', '**')
    funcao = funcao.replace("ln", "log") 
    

    ambiente = {"__builtins__": None, "x": x}
    
    for nome in dir(math):
        if not nome.startswith("_"):  
            ambiente[nome] = getattr(math, nome)

    return eval(funcao, ambiente)

