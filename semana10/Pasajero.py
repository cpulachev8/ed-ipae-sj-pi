class Pasajero:

    def __init__(self) -> None:
        pass
    
    def read(self) -> None:
        print("**** DATOS DEL PASAJERO ****")
        self.dni = input("DNI: ")
        self.nombres = input("Nombres: ")
        self.celular = input("Celular: ")
    
    def save(self) -> None:
        f_pasajeros = open("pasajeros.txt", "a")
        f_pasajeros.write("{},{},{}\n".format(self.dni, self.nombres, self.celular))
        f_pasajeros.close()
    
    def format(self, cadena: str):
        datos = cadena.split(",")
        self.dni = datos[0]
        self.nombres = datos[1]
        self.celular = datos[2]
        return self

    def _print(self):
        print("DNI: {} \tNombres: {}\tCelular:{}".format(self.dni, self.nombres, self.celular), end="")

    def find(self, dni: str) -> bool:
        return self.dni == dni
