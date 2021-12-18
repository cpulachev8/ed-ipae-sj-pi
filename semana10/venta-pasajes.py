
# Ingresar los pasajeros
from Pasajero import Pasajero

def main_menu():
    print("***** MENU PRINCIPAL *****")
    print("[1] Agregar Pasajero")
    print("[2] Mostrar Pasajeros")
    print("[3] Buscar Pasajero")
    print("[4] Vender Pasaje")
    print("[X] Salir")

def to_list_pasajeros():
    pasajeros = read_pasajeros()
    for pasaj in pasajeros:
        pasaj._print()

def read_pasajeros():
    pasajeros = []
    f_pasajeros = open("pasajeros.txt", "r")
    lines = f_pasajeros.readlines()    
    for line in lines:        
        pasajero = Pasajero()
        pasajeros.append(pasajero.format(line))
    return pasajeros

def find_pasajero(dni_search: str):
    pasajeros = read_pasajeros()
    for pasaj in pasajeros:
        if (pasaj.find(dni_search)):
            print("Pasajero encontrado")
            pasaj._print()

while True:
    main_menu()
    opc = input("Ingrese Opción: ")    
    if opc == "1": 
        pasajero = Pasajero()
        pasajero.read()       
        pasajero.save()
    elif opc == "2":
        print("Lista de Pasajeros")
        to_list_pasajeros()
    elif opc == "3":
        dni_search = input("DNI a buscar: ")
        find_pasajero(dni_search)
    else:
        break

# Crear el archivo pasajeros
# file = open("pasajeros.txt", "w")
# file.close
