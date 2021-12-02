from Figura import Figura


class Triangulo(Figura):

    def __init__(self) -> None:
        super().__init__()
        self.nombre_fig = "Triángulo"
        self.nro_lados = 3
        self.color = "Amarillo"
        self.base = int(input("Ingrese base: "))
        self.altura = int(input("Ingrese altura: "))

    def calcular_area(self) -> float:
        return self.base * self.altura / 2