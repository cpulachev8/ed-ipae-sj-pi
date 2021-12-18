class Pasajero:

    def __init__(self) -> None:
        print("**** DATOS DEL PASAJERO ****")
        self.dni = input("DNI: ")
        self.nombres = input("Nombres: ")
        self.celular = input("Celular: ")
    
    def grabar(self) -> None:
        f_pasajeros = open("pasajeros.txt", "a")
        f_pasajeros.write("{},{},{}\n".format(self.dni, self.nombres, self.celular))
        f_pasajeros.close()