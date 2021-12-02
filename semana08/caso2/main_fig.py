from Cuadrado import Cuadrado
from Rombo import Rombo
from Triangulo import Triangulo
from Circulo import Circulo

print("***** Datos del cuadrado ******")
cuad = Cuadrado()
print("***** Datos del triángulo ******")
trian = Triangulo()
print("***** Datos del rombo ******")
rombo = Rombo()
print("***** Datos del Círculo ******")
circulo = Circulo()

print("***** Datos de las figuras ******")
print("***** Datos del cuadrado ******")
cuad.mostrar_datos()
print("Su perímetro es", cuad.calcular_perimetro())
print("Su área es", cuad.calcular_area())
print()
print("***** Datos del triángulo ******")
trian.mostrar_datos()
print("Su área es", trian.calcular_area())
print()
print("***** Datos del rombo ******")
rombo.mostrar_datos()
print("Su área es", rombo.calcular_area())
print()
print("***** Datos del círculo ******")
circulo.mostrar_datos()
print("Su área es", circulo.calcular_area())
print()
