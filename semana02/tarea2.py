import calculadora
# 1. Idenfificar las operaciones
# 2. Identificar los números ingresados.
# 3. Realizar las operaciones sobre los números
numeros = []
operadores = ["+", "-", "*", "/"]
prioridad1 = ["*", "/"]
prioridad2 = ["+", "-"]

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
        a = calculadora.operar(operaciones[1], numeros[1], numeros[2])
        return calculadora.operar(operaciones[0], numeros[0], a)
    else:
        a = calculadora.operar(operaciones[0], numeros[0], numeros[1])
        return calculadora.operar(operaciones[1], a, numeros[2])    

entrada = input("Ingrese operación: ")
operaciones = []
leer(entrada)
print(operaciones)
print(numeros)
print("El resultado de la operación es {}".format(operar()))