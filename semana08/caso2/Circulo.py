from Figura import Figura

class Circulo(Figura):

    def __init__(self) -> None:
        super().__init__()
        self.nombre_fig = "Círculo"
        self.color = "Verde"
        self.radio = int(input("Radio: "))

    def calcular_area(self) -> float:
        return 3.14 * (self.radio ** 2)