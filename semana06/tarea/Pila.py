class Pila:   

    def __init__(self) -> None:
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        valor = self.items[-1]
        del self.items[-1]
        return valor