# ********* SIN USO DE LAMBDAS **********
# def sumar(a, b):
#     return a + b

# print("5 + 3 = ", sumar(5, 3))

# ********* CON USO DE LAMBDAS **********
# funcion = lambda x : "El valor es: " + x
# print(funcion(input("Ingrese un valor: ")))

sum = lambda a, b : a + b
resultado = lambda a, b: "{} + {} = {}" .format(a, b, sum(a, b))
# print(resultado(5,3, 8))
print(resultado(int(input("Primer valor: ")), int(input("Segundo valor: "))))

mayor_edad = lambda edad : "Es mayor de edad" if edad > 18 else "No es mayor de edad"
print(mayor_edad(int(input("Ingrese su edad: "))))

# import datetime

# def mayor_edad():
#     # ingrese su fecha de nacimiento
#     fec_nac = input("Ingrese fecha Nacimiento")
#     # calcular su edad
#     print(datetime.datetime.today())
#     # devolver si es mayor de edad

# mayor_edad()