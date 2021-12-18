
# Ingresar los pasajeros
from Pasajero import Pasajero

# Crear el archivo pasajeros
file = open("pasajeros.txt", "w")
file.close

pasajeros = []
for i in range(5):
    pasajero = Pasajero()
    pasajeros.append(pasajero)
    pasajero.grabar()