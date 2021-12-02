class Cliente:
    
    def __init__(self) -> None:
        self.nombre = input("Nombre del Cliente: ")
        self.saldo = 0.0

    def depositar(self, monto: float) -> None:
        self.saldo += monto
    
    def retirar(self, monto: float) -> None:
        if self.consultar_saldo() >= monto:
            self.saldo -= monto

    def consultar_saldo(self) -> float:
        return self.saldo