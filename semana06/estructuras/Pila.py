class Pila:   

    def __init__(self) -> None:
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        valor = self.items[-1]
        del self.items[-1]
        return valor

monedas = Pila()
monedas.push("S/ 5.00")
monedas.push("S/ 1.00")
monedas.push("S/ 2.00")
monedas.push("S/ 2.00")
monedas.push("S/ 0.50")

print(monedas.pop())
print(monedas.pop())

print(monedas.items)