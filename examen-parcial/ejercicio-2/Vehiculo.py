class Vehiculo:

    def __init__(self) -> None:
        print("Datos del vehículo")
        self.marca = input("Marca: ")
        self.modelo = input("Modelo: ")
        self.km = input("Kilometraje: ")
        self.precio = float(input("Precio: "))

    def obtener_precio(self) -> float:
        return self.precio

    def print(self) -> None:
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Kilometraje: ", self.km)        