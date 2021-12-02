from Figura import Figura


class Rombo(Figura):

    def __init__(self) -> None:
        super().__init__()
        self.nombre_fig = "Rombo"
        self.nro_lados = 4
        self.color = "Rojo"
        self.diag_mayor = int(input("Diagonal mayor: "))
        self.diag_menor = int(input("Diagonal menor: "))

    def calcular_area(self) -> float:
        return self.diag_mayor * self.diag_menor / 2