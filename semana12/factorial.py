number = int(input("Número a calcular factorial: "))

# Algoritmo sin recursividad para calcular factorial
# fact = 1
# for i in range(1,number + 1,1):
#     fact *= i
# print("El factorial de {} = {}".format(number, fact))


# Algoritmo usando recursividad para calcular factorial
# 1. Debe invocar al mismo método
# 2. Siempre retorna un valor
# 3. Para evitar el bucle infinito, debe tener un punto de corte
def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

fact = factorial(number)
print("El factorial de {} = {}".format(number, fact))