from django.shortcuts import render

def home(request):
    return render(request, 'calculo_integral/home.html') #ter que fazer esse html
def calcular_integral(request):
    if request.method == "POST":
        try:
            funcao = request.POST.get('funcao')
            a = float(request.POST.get('Limite inferior'))
            b = float(request.POST.get('limite_superior'))
            n = int(request.POST.get('num_retangulos', 1000))
            # vai ser por metodo dos retangulos
        except Exception as e:
            # definir o except depois 