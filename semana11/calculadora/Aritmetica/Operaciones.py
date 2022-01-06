def sumar(a: int, b: int):
    return a + b

def restar(a: int, b: int):
    return a - b

def multiplicar(a: int, b: int):
    return a * b

def dividir(a: int, b: int):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: División por cero")