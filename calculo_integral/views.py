from django.shortcuts import render
from django.http import JsonResponse
import math
import re

def home(request):
    return render(request, 'calculo_integral/home.html') #ter que fazer esse html
def calcular_integral(request):
    if request.method == "POST":
        try:
            funcao = request.POST.get('funcao')
            a = float(request.POST.get('Limite inferior'))
            b = float(request.POST.get('limite_superior'))
            tolerancia = float(request.POST.get('tolerancia', 1e-6))
            metodo = request.POST.get('metodo', 'meio') 

            resultado = soma_rieamann(funcao, a, b, n) 

            context = {
                'resultado' : resultado,
                'funcao' : funcao,
                'limite_inferior' : a,
                'limite_superior' : b,
                'numero_retangulos' : n  
            }

            return render(request, 'calculo_integral/resultado.html', context) 
        #html tambem precisa ser feito 
    
        except Exception as e:
            return render(request, 'calcular_integral/home.html',{
                'erro' : f'Erro nesse calculo: {str:(e)}'
            })
    
    return render(request,'calcular_integral/home.html')
def soma_rieamann(funcao_str, a, b, n):
   # Vai calcular a integral usaando método dos retângulos
   h = (b - a) / n #largura dos retangulos
   soma = 0

   for i in range(n):
       x = a + i * h + h/2
       try:
           y = ajeita_funcao(funcao_str, x) 
           soma += y * h
       except:
           continue
   return soma

def ajeita_funcao(funcao_str, x):
    #para nao ter erro na hora de resolver
    funcao = funcao_str.replace('^', '**')
    funcao = funcao.replace('sen', 'math.sin')
    funcao = funcao.replace('cos', 'math.cos')
    funcao = funcao.replace('tan', 'math.tan')
    funcao = funcao.replace('log', 'math.log')
    funcao = funcao.replace('ln', 'math.log')
    funcao = funcao.replace('exp', 'math.exp')
    funcao = funcao.replace('sqrt', 'math.sqrt')
    funcao = funcao.replace('pi', 'math.pi')
    funcao = funcao.replace('e', 'math.e')

    allowed_names = {
        "x" : x,
        "math": math,
        "abs" : abs,
        "pow" : pow
    }

    return eval(funcao, {"__builtins__": {}}, allowed_names)
