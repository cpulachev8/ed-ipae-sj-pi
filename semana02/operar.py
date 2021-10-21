# uso de la calculadora
# Primera operación: con 20 y 4

import calculadora

calculadora.imprimir("suma", calculadora.sumar(20, 4))
calculadora.imprimir("resta", calculadora.restar(20,4))
calculadora.imprimir("multiplicación", calculadora.multiplicar(20,4))
calculadora.imprimir("división", calculadora.dividir(20,4))

# Resolver (3 + 5)*10
val1 = calculadora.sumar(3, 5)
calculadora.imprimir("operación", calculadora.multiplicar(val1, 10))