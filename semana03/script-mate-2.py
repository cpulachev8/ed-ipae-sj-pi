from matematica import geometria
from matematica import calculadora

try:
    lado = int(input("Ingresar lado del cuadrado: "))
    print("El perímetro del cuadro de lado {} es {}".format(lado, geometria.perimetro_cuadrado(lado)))

    num1 = int(input("Ingrese un valor: "))
    num2 = int(input("Ingrese otro valor: "))
    print("La división de los números ingresados es", calculadora.division(num1, num2))
except TypeError:
    print("Se ingresó un valor incorrecto") 
except ZeroDivisionError:
    print("No es posible realizar una división por cero")
    # num2 = 1
    # print("La división de los números ingresados es", calculadora.division(num1, num2))
except:
    print("Ocurrió un error")   

