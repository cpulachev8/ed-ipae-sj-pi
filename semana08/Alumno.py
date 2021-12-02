from Persona import Persona


class Alumno(Persona):

    def __init__(self) -> None:
        super().__init__()
        self.tipo = "Alumno"
        self.grado = input("Ingrese grado: ")

    def imprimir(self) -> None:
        super().imprimir()
        print("Grado: ", self.grado)

    def funcion_principal(self) -> None:
        print("Su función principal es ESTUDIAR")