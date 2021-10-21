# uso de la calculadora
# Primera operación: con 20 y 4

import calculadora

calculadora.imprimir("suma", calculadora.sumar(20, 4))
calculadora.imprimir("resta", calculadora.restar(20,4))
calculadora.imprimir("multiplicación", calculadora.multiplicar(20,4))
calculadora.imprimir("división", calculadora.dividir(20,4))

# Resolver (3 + 5)*10
calculadora.imprimir("operación", calculadora.multiplicar(calculadora.sumar(3, 5), 10))
calculadora.imprimir("Potencia", calculadora.potencia(5,2))

# Tarea: Crear el archivo operacion_combinada.py que permita leer una cadena que representa los cálculos que se deben realizar con el módulo de calculadora. Mínimo debe permitir trabajar con 3 números. Debe imprimir el resultado de la operación
# Por ejemplo: 4+5*10 = 54
# En caso se ingrese una cadena que no se puede operar imprimir un mensaje de error. P.e. +9*5-
# Plazo hasta el lunes