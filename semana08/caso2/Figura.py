class Figura:

    def __init__(self) -> None:
        self.nombre_fig = ""
        self.nro_lados = 0
        self.color = "Sin color"

    def mostrar_datos(self) -> None:
        print("Figura ", self.nombre_fig)
        print("Lados ", self.nro_lados)
        print("Color ", self.color)

    def calcular_perimetro(self) -> float:
        pass

    def calcular_area(self) -> float:
        pass