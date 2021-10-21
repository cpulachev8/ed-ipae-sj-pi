def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def fib(n):
    a, b, c = 0, 1, 0
    while b < n:
       print(b, end = " ")
       # c = b
       # b = a + b
       # a = c
       a, b = b, a + b
    print()

def imprimir(operacion, resultado):
    print("La %s es: %d"% (operacion, resultado))