# try:
#     a = int(input("Ingrese número"))
#     div = a / 5
# except KeyboardInterrupt:
#     print("Está intentando finalizar el programa")
# except:
#     print("Estimado usuario, ocurrió en error")
# else:
#     print("El programa se ejecutó con éxito")
# finally:
#     print("Finalizó el programa")

# Excepciones a medida

class TamanioDNI(Exception):

    def __init__(self, dni) -> None:
        super().__init__(self)
        self.dni = dni
        self.tamanio = len(dni)
    
    def get_message(self) -> str:
        return "DNI incorrecto. Excede el tamaño permitido. DNI actual tiene {} caracteres".format(self.tamanio)

try:
    dni = input("Ingrese DNI: ")
    if (len(dni) != 8):
        raise TamanioDNI(dni)
except TamanioDNI as td:
    print(td.get_message())
