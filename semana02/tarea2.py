entrada = input("Ingrese operación: ")
operaciones = []
# 1. Idenfificar las operaciones
# 2. Identificar los números ingresados.
# 3. Realizar las operaciones sobre los números
numeros = []

def buscar_operacion(signo, funcion, prioridad):
    if (entrada.__contains__(signo)):
        operacion = {"operacion": funcion, "prioridad": prioridad}
        operaciones.append(operacion)

def is_int(val):
    try:
        int(val)
        return True
    except:
        return False

buscar_operacion("+", "suma", 2)
buscar_operacion("-", "resta", 2)
buscar_operacion("*", "producto", 1)
buscar_operacion("/", "division", 1)

for oper in operaciones:
    print(oper)
    if (oper["prioridad"] == 1):
        if (oper["operacion"] == "producto"):
            print("Hay producto")
            valores = entrada.split("*")
            for v in valores:
                if is_int(v):
                    numeros.append(v)
                else:
                    valores = entrada.split("*")
                    for vl in valores:
                        numeros.append(vl)


print(numeros)
