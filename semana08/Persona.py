class Persona:

    def __init__(self) -> None:
        self.nombre = input("Ingrese nombre: ")
        self.sexo = input("Ingrese sexo: ")
        self.edad = input("Ingrese edad: ")
        self.tipo = "No identificado"

    def imprimir(self) -> None:
        print("Nombre: ", self.nombre)
        print("Sexo: ", self.sexo)
        print("Edad: ", self.edad)
        print("Tipo: ", self.tipo)

    def funcion_principal(self) -> None:
        pass