# Calculadora de Integral

Sistema web que calcula integrais usando o **Método dos Retângulos**.

Projeto desenvolvido para a disciplina de Cálculo II.

Professor: Renan Santos

LINK VIDEO:

## Como rodar

```bash
#Instalar dependências
pip install -r requirements.txt

#Configurar banco
python manage.py makemigrations
python manage.py migrate

#Rodar servidor
python manage.py runserver
```

Acesse: `http://127.0.0.1:8000/`

## Como usar

1. Digite uma função (ex: `x**2`)
2. Coloque os limites (ex: de `0` a `1`)
3. Clique "Calcular"

## Testes

```bash
python manage.py test calculo_integral
```

**7 testes validam:**
- ∫5 dx = 10 
- ∫x dx = 2   
- ∫x² dx = 0.333 
- ∫sin(x) dx = 2  

**Método**: Divide a área em retângulos pequenos e soma tudo.

Feito para calcular integrais de funções elementares com precisão.