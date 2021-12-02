from Persona import Persona

class Docente(Persona):

    def __init__(self) -> None:
        super().__init__()
        self.tipo = "Docente"
        self.univ_egreso = input("Ingrese universidad que egresó: ")
    
    def imprimir(self) -> None:
        super().imprimir()
        print("Universidad que egresó: ", self.univ_egreso)
    
    def funcion_principal(self) -> None:
        print("Su función principal es ENSEÑAR")