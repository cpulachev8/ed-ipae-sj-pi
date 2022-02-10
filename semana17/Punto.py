class Punto:

    def __init__(self, x, y) -> None:
        try:
            self.x = float(x)
            self.y = float(y)
        except:
            print("Datos incorrectos. Se inicializa en cero")
            self.x = 0.0
            self.y = 0.0

    def print(self) -> None:
        print("Punto (x={}, y={}) pertenece al {}".format(self.x, self.y, self.pertenece_al_cuadrante()))

    def pertenece_al_cuadrante(self) -> str:        
        if self.x > 0 and self.y > 0: # Cuadrante I
            return "CUADRANTE I"
        elif self.x < 0 and self.y > 0: # Cuadrante II
            return "CUADRANTE II"
        elif self.x < 0 and self.y < 0: # Cuadrante III
            return "CUADRANTE III"
        elif self.x > 0 and self.y < 0: # Cuadrante IV
            return "CUADRANTE IV"
        else:
            return "CUADRANTE NO DEFINIDO"

# punto1 = Punto(input("Ingrese X: "), input("Ingrese Y: "))
# punto1.print()