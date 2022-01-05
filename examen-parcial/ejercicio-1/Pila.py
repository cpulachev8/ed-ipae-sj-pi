class Pila:

    def __init__(self) -> None:
        self.items = []

    def push(self, element) -> None:
        self.items.append(element)

    def pop(self):
        valor = self.items[-1]
        del self.items[-1]
        return valor

    def print(self) -> None:
        print(self.items)

    def isEmpty(self) -> bool:
        return len(self.items) == 0