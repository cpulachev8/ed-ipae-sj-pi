from Persona import Persona
from Alumno import Alumno
from Docente import Docente

print("******** Registrando persona ********")
persona1 = Persona()
print()

print("******** Registrando alumno ********")
alumno1 = Alumno()
print()

print("******** Registrando docente ********")
docente = Docente()

# Sobrecarga de métodos con herencia - reutilización
print("******** Imprimiendo datos ingresados ********")
print("========== Persona ==========")
persona1.imprimir()
print("========== Alumno ==========")
alumno1.imprimir()
print("========== Docente ==========")
docente.imprimir()
print()

# Sobreescritura de métodos con herencia - cambiar el comportamiento
print("******** Funciones principales ********")
persona1.funcion_principal()
alumno1.funcion_principal()
docente.funcion_principal()
