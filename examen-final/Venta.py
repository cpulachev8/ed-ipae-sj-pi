from datetime import datetime
from DetalleVenta import DetalleVenta

class Venta:

    def __init__(self, cliente: str, medio_pago: str) -> None:
        self.cliente = cliente
        self.fecha = datetime.today()
        self.total = 0
        self.medio_pago = medio_pago
        self.recargo = 0
        self.detalles = []

    def imprimir(self):
        print("===================================")
        print("Cliente: {}".format(self.cliente))
        print("Fecha Venta: {}".format(self.fecha.strftime("%d-%m-%Y")))
        print("Total Venta: {}".format(self.total))
        print("Medio Pago: {}".format(self.medio_pago))
        print("Recargo: {}".format(self.recargo))
        print("***** DETALLES *****")
        for i in range(len(self.detalles)):
            print("[{}] ----------------------".format(i+1))
            self.detalles[i].imprimir()
        print("===================================")

    def agregar_detalle(self, producto: str, cantidad: int, precio_unitario: float):
        dv = DetalleVenta(producto, cantidad, precio_unitario)
        self.detalles.append(dv)

    def calcular_recargo(self):        
        if str.lower(self.medio_pago) == "tarjeta":
            self.calcular_total()
            self.recargo = self.total * 0.05

    def calcular_total(self):
        tot_aux = 0.0
        for det in self.detalles:
            tot_aux += det.total
        self.total = tot_aux + self.recargo
