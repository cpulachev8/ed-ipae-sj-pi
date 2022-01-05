from Auto import Auto
from Moto import Moto

def show_menu() -> int:
    try:
        while True:
            print("********** Tipo Vehículo **********")
            print("[1] Auto")
            print("[2] Moto")
            option = int(input("Opción: "))
            if option == 1 or option == 2:
                return option
            else:
                print("Error: Opción incorrecta")
    except:
        print("Error: Opción incorrecta")
    

def fillVehicles():
    for i in range(vehicles_number):
        option = show_menu()
        if option == 1:
            vehicles.append(Auto())
        elif option == 2:
            vehicles.append(Moto())

def print_vehicles():
    print("********** Vehículos Ingresados **********")
    for veh in vehicles:
        veh.print()

vehicles = []
vehicles_number = int(input("Cantidad de vehículos a ingresar: "))
fillVehicles()
print_vehicles()