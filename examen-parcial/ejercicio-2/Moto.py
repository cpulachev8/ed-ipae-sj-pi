from Vehiculo import Vehiculo

class Moto(Vehiculo):
    
    def __init__(self) -> None:
        super().__init__()
        self.casco = input("¿Con casco? ")

    def obtener_precio(self) -> float:
        if self.casco.lower() == "si":
            return self.precio + 80
        return super().obtener_precio()

    def print(self) -> None:
        print("**** Datos de la Moto ****")
        super().print()
        print("Con casco: ", self.casco)
        print("Precio: ", self.obtener_precio())