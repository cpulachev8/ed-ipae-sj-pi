def llenar():
    n = 3
    i = 0
    while i < n :
        lista.append(input("Ingrese número "))
        i = i + 1

def mostrar_elemento():    
    try:
        pos = int(input("Ingrese posición a mostrar: "))
        print(lista[pos])
    except ValueError:
        print("No ingresó un valor correcto")
    except IndexError:
        print("La posición ingresada no existe")
    except:
        print("Ocurrió un error")

lista = []
llenar()
mostrar_elemento()