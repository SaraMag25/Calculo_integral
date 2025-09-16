from django.shortcuts import render
from django.http import JsonResponse
import math
import re

def home(request):
    return render(request, 'calculo_integral/home.html') 
def calcular_integral(request):
    if request.method == "POST":
        try:
            funcao = request.POST.get('funcao', '').strip()
            a = float(request.POST.get('limite_inferior'))
            b = float(request.POST.get('limite_superior'))
            tolerancia = float(request.POST.get('tolerancia', 1e-6))

            resultado, n_usado, erro_estimado = calcular_integral_adaptativa(funcao, a, b tolerancia) #criar tal funcao

            # Tem que salvar no banco
            from .models import CalculoIntegral
            calculo = CalculoIntegral.objects.create(
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
# def soma_rieamann(funcao_str, a, b, n):
#    # Vai calcular a integral usaando método dos retângulos
#    h = (b - a) / n #largura dos retangulos
#    soma = 0

#    for i in range(n):
#        x = a + i * h + h/2
#        try:
#            y = ajeita_funcao(funcao_str, x) 
#            soma += y * h
#        except:
#            continue
#    return soma

# def ajeita_funcao(funcao_str, x):
#     #para nao ter erro na hora de resolver
#     funcao = funcao_str.replace('^', '**')
#     funcao = funcao.replace('sen', 'math.sin')
#     funcao = funcao.replace('cos', 'math.cos')
#     funcao = funcao.replace('tan', 'math.tan')
#     funcao = funcao.replace('log', 'math.log')
#     funcao = funcao.replace('ln', 'math.log')
#     funcao = funcao.replace('exp', 'math.exp')
#     funcao = funcao.replace('sqrt', 'math.sqrt')
#     funcao = funcao.replace('pi', 'math.pi')
#     funcao = funcao.replace('e', 'math.e')

#     allowed_names = {
#         "x" : x,
#         "math": math,
#         "abs" : abs,
#         "pow" : pow
#     }

#     return eval(funcao, {"__builtins__": {}}, allowed_names)
