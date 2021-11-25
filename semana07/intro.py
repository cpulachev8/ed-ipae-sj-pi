# Repaso de métodos propios de python
# cadena = "1,2,3,4,5"
# list = cadena.split(",")
# print(cadena)
# print(list)

# uso del método __init__ de una clase
from Persona import Persona

print("****** PERSONA UNO **********")
persona1 = Persona()
persona1.imprimir_datos()
persona1.imprimir_mayor_edad()
persona1.apto_licencia_conducir()

print("****** PERSONA DOS **********")
persona2 = Persona()
persona2.imprimir_datos()
persona2.imprimir_mayor_edad()
persona2.apto_licencia_conducir()