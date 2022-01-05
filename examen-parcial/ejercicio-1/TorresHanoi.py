from Pila import Pila

class TorresHanoi:

    def __init__(self) -> None:
        self.tower_one = Pila()
        self.tower_two = Pila()
        self.tower_three = Pila()
        self.disk_number = int(input("Ingrese número de discos: "))
        self.movements_number = 0
        self.enter_tower_one()
        print("********* Iniciando el Juego *********")
        self.print_towers()

    def enter_tower_one(self):
        for i in range(self.disk_number, 0, -1):
            self.tower_one.items.append(i)

    def start_play(self) -> None:    
        while(not self.play_end()):
            self.movements_number += 1
            self.request_play()            
        else:
            if self.min_movements_number() == self.movements_number:
                print("****** FELICITACIONES GANÓ. MEJOR RÉCORD DE JUGADAS **********")
            else:
                print("****** FELICITACIONES GANÓ **********")

    def request_play(self) -> None:
        tower_source = int(input("Torre Origen: "))
        tower_destination = int(input("Torre destino: "))
        self.move_disk(self.get_tower(tower_source), self.get_tower(tower_destination))

    def move_disk(self, tower_source: Pila, tower_destination: Pila) -> None:
        if not tower_source.isEmpty():        
            disk = tower_source.pop()
            
            if (not tower_destination.isEmpty()):
                disk_last = tower_destination.pop()
                if (disk < disk_last):
                    tower_destination.push(disk_last)
                    tower_destination.push(disk)
                else:
                    print("Movimiento erróneo")
                    tower_destination.push(disk_last)
                    tower_source.push(disk)
            else:
                tower_destination.push(disk)        
        else:
            print("Torre origen está vacía")

        self.print_towers()

    def get_tower(self, tower_number) -> Pila:
        if (tower_number == 1):
            return self.tower_one
        if (tower_number == 2):
            return self.tower_two
        if (tower_number == 3):
            return self.tower_three

    def print_towers(self) -> None:
        print("Torre 1: ", end="")
        self.tower_one.print()
        print("Torre 2: ", end="")
        self.tower_two.print()
        print("Torre 3: ", end="")
        self.tower_three.print()
        print("Número de jugadas: ", self.movements_number)

    def play_end(self) -> bool:
        return self.tower_one.isEmpty() and self.tower_two.isEmpty()
    
    def min_movements_number(self) -> int:
        return 2 ** self.disk_number - 1
