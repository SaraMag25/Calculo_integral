from django.shortcuts import render

def home(request):
    return render(request, 'calculo_integral/home.html') #ter que fazer esse html
def calcular_integral(request):
    if request.method == "POST":
        try:
            funcao = request.POST.get('funcao')
            a = float(request.POST.get('Limite inferior'))
            b = float(request.POST.get('limite_superior'))
            n = int(request.POST.get('numero_retangulos', 1000))

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
def soma_riemann(funcao_str, a, b, n):
   # Vai calcular a integral usaando método dos retângulos
   h = (b - a) / n #largura dos retangulos
   soma = 0

   for i in range(n):
       x = a + i * h + h/2
       try:
           y = avaliar_funcao(funcao_str, x) #fazer essa funcao
           soma += y * h
       except:
           continue
       
    return soma