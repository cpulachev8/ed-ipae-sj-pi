from math import pow

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def operar(signo, a, b):
    if signo == "+":
        return sumar(a, b)
    elif signo == "-":
        return restar(a,b)
    elif signo == "*":
        return multiplicar(a,b)
    elif signo == "/":
        return dividir(a,b)


def potencia(a, b):
    return pow(5, 2)

def fib(n):
    a, b, c = 0, 1, 0
    while b < n:
       print(b, end = " ")
       # c = b
       # b = a + b
       # a = c
       a, b = b, a + b
    print()

# Para formatear:
# %s texto o cadena
# %d decimales o números
def imprimir(operacion, resultado):
    print("La %s es: %d"% (operacion, resultado))