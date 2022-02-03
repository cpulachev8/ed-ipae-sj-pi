# Solución de Elías Tagle
# def es_potencia(n,b):
#     for i in range(n):
#         print(b**i)
#         if b**i == n:
#             return True
#     else:
#         return False

# n = int(input("Ingrese n: "))
# b = int(input("Ingrese b: "))
# print(es_potencia(n, b))
# print(es_potencia(64,4))
# print(es_potencia(70,10))



def es_potencia(n: int, b:int) -> bool:
    exponente = 0
    aux = 0
    while aux < n:
        aux = b ** exponente
        print(aux)
        if aux == n:
            return True
        exponente += 1
    return False

# n = int(input("Ingrese n: "))
# b = int(input("Ingrese b: "))
# print(es_potencia(n, b))