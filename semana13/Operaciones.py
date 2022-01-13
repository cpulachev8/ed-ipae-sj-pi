# Pruebas unitarias (Unit Test) - coverage (Nivel de cobertura)
# Pruebas unitarias son realizadas por el desarrollador
# Los analistas de calidad (QA) realizan pruebas manuales o pruebas automatizadas.

def operar(operacion, a, b):
    if operacion == "+":
        return sumar(a, b)
    if operacion == "-":
        return restar(a, b)
    if operacion == "/":
        return dividir(a,b)
    print("Operacion desconocida")
    return -1

def sumar(a,b):    
    return a + b

def dividir(a, b):
    return a / b

def restar(a, b):
    return a - b