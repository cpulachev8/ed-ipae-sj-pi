# Iteraciones

# palabra = "Ingeniería"
# for letra in palabra:
#     print(letra)
# for letra in palabra[::-1]:
#     print(letra)
# for idx in range(len(palabra)):
#     print("{} - {}".format(idx, palabra[idx]))

lista = [1, 2, 3, 4, 5]
# for item in lista:
#     print(item)
# for item in lista[::-2]:
#     print(item)
# try:
#     it_lista = iter(lista)
#     while True:
#         print(it_lista.__next__())
# except StopIteration:
#     print("Termino el recorrido de la lista")


# Iterar un diccionario
# dicc = {"Marca": "Lenovo", "Modelo": "ThinkPad", "Procesador": "Core I7", "Memoria": "20Gb"}
# for clave, valor in dicc.items():
#     print(clave, " : ", valor)

# Generadores yield

a = 0
def gen_basico():
    yield "Fútbol"
    a = 1 + 2
    a += 100
    yield "Vóley"
    a = 4 * 5
    print ("Valor de a = ", a)
    yield "Básquet"
    # return ["Fútbol", "Vóley"]

for dep in gen_basico():
    print(dep)

print ("Valor de a = ", a)   

