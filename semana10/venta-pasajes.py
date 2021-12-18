
# Ingresar los pasajeros
from Pasajero import Pasajero

# Crear el archivo pasajeros
file = open("pasajeros.txt", "w")
file.close

for i in range(5):
    pasajero = Pasajero()
    pasajero.grabar()