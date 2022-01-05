from Vehiculo import Vehiculo

class Auto(Vehiculo):
    
    def __init__(self) -> None:
        super().__init__()
        self.airbag = input("¿Con airbag? ")

    def obtener_precio(self) -> float:
        if self.airbag.lower() == "si":
            return self.precio + 300
        return super().obtener_precio()

    def print(self) -> None:
        print("**** Datos del Auto ****")
        super().print()
        print("Con airbag: ", self.airbag)
        print("Precio: ", self.obtener_precio())