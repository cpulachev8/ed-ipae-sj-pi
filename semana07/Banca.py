class Cliente:
    
    def __init__(self) -> None:
        self.nombre = input("Nombre del Cliente: ")
        self.saldo = 0.0

    def depositar(self, monto) -> None:
        # self.saldo = self.saldo + monto
        self.saldo += monto
    
    def retirar(self, monto) -> None:
        self.saldo -= monto

    def consultar_saldo(self) -> float:
        return self.saldo

class Banco:
    def __init__(self) -> None:
        self.cliente1 = Cliente()
        self.cliente2 = Cliente()
        self.cliente3 = Cliente()

    def operaciones(self) -> None:
        self.cliente1.depositar(100)
        self.cliente2.depositar(50)
        self.cliente1.retirar(70)
        self.cliente3.depositar(200)

    def depositos_totales(self) -> float:
        return self.cliente1.consultar_saldo() + self.cliente2.consultar_saldo() + self.cliente3.consultar_saldo()