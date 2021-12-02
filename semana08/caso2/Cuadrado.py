from Figura import Figura


class Cuadrado(Figura):

    def __init__(self) -> None:
        super().__init__()
        self.nombre_fig = "Cuadrado"
        self.nro_lados = 4
        self.color = "Azul"
        self.tam_lado = int(input("Medida del lado: "))

    def calcular_perimetro(self) -> float:
        return self.nro_lados * self.tam_lado

    def calcular_area(self) -> None:
        return self.tam_lado ** 2