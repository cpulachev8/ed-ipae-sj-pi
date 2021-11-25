from Pila import Pila

cant = int(input("Cantidad de contenedores: "))
contenedores = Pila()

def llenar_contenedores():
    for i in range(cant):
        contenedor = input("Contenedor {}: ".format(i+1))
        contenedores.items.append(contenedor)


def retirar_contenedor(contenedor):    
    try:
        pila_aux = Pila()
        cont_ret = contenedores.pop()    
        idx = contenedores.items.index(contenedor)
        if idx > 0:
            while cont_ret != contenedor:
                pila_aux.push(cont_ret)
                cont_ret = contenedores.pop()

            while len(pila_aux.items) > 0:
                contenedores.push(pila_aux.pop())
    except:
        print("Contenedor no encontrado")

llenar_contenedores()
print("Contenedores llenados", contenedores.items)
cont_retirar = input("Contenedor a retirar: ")
retirar_contenedor(cont_retirar)
print("Contenedores actualizado: ", contenedores.items)