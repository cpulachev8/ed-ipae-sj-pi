import calculadora
# 1. Leer la cadena
# 2. Idenfificar las operaciones
# 3. Identificar los números ingresados.
# 4. Realizar las operaciones sobre los números
numeros = []
operadores = ["+", "-", "*", "/"]
prioridad1 = ["*", "/"]

def leer(cadena):
    numero = ""
    for i in range(len(cadena)):
        if is_int(cadena[i]):
            numero += cadena[i]
        elif cadena[i] in operadores:
            operaciones.append(cadena[i])
            numeros.append(int(numero))
            numero = ""
        else:
            print("Error en cadena")
            break
        if i == len(cadena) - 1:
            numeros.append(int(numero))


def is_int(val):
    try:
        int(val)
        return True
    except:
        return False

def operar():
    if operaciones[1] in prioridad1:
        a = operar_calculadora(operaciones[1], numeros[1], numeros[2])
        return operar_calculadora(operaciones[0], numeros[0], a)
    else:
        a = operar_calculadora(operaciones[0], numeros[0], numeros[1])
        return operar_calculadora(operaciones[1], a, numeros[2])  

def operar_calculadora(signo, a, b):
    if signo == "+":
        return calculadora.sumar(a, b)
    elif signo == "-":
        return calculadora.restar(a,b)
    elif signo == "*":
        return calculadora.multiplicar(a,b)
    elif signo == "/":
        return calculadora.dividir(a,b)  

# Bloque principal
entrada = input("Ingrese operación: ")
operaciones = []
leer(entrada)
print(operaciones)
print(numeros)
print("El resultado de la operación es {}".format(operar()))