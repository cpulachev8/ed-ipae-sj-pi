class DetalleVenta:

    def __init__(self, producto: str, cantidad: int, precio_unitario: float) -> None:
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.descuento = 0.0
        self.total = 0.0
        if self.tiene_descuento():
            self.calcular_descuento()
        self.calcular_total()

    def imprimir(self):
        print("\tProducto: {}".format(self.producto))
        print("\tCantidad: {}".format(self.cantidad))
        print("\tPrecio Unitario: {}".format(self.precio_unitario))
        print("\tDescuento: {}".format(self.descuento))
        print("\tTotal: {}".format(self.total))

    def tiene_descuento(self)-> bool :
        return str.lower(self.producto) in ["arroz", "aceite"]

    def calcular_descuento(self):
        self.descuento = (self.cantidad * self.precio_unitario) * 0.25
    
    def calcular_total(self):
        self.total = (self.cantidad * self.precio_unitario) - self.descuento