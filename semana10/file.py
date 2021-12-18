# ************** ESCRITURA DE ARCHIVOS *******************
file_datos = open("datos_personales.txt", "w")
file_datos.write("Christian Jhonathan\n")
file_datos.write("Pulache Viera\n")
file_datos.write("Peruana\n")
file_datos.write("Ingeniero informático")
file_datos.close()


# ************** LECTURA DE ARCHIVOS *******************
# ************** TODO EL CONTENIDO *******************
# file_datos = open("datos_personales.txt", "r")
# content = file_datos.read()
# print(content)
# file_datos.close()

# ************** LECTURA DE ARCHIVOS *******************
# ************** LÍNEA POR LÍNEA *******************
# file_datos = open("datos_personales.txt", "r")
# line = file_datos.readline()
# while len(line) > 0:
#     print(line, end = "")
#     line = file_datos.readline()
# file_datos.close()

# ************** LECTURA DE ARCHIVOS *******************
# ************** TODAS LAS LINEAS *******************
# file_datos = open("datos_personales.txt", "r")
# lines = file_datos.readlines()
# for line in lines:
#     print(line, end = "")
# file_datos.close()

# ************** AGREGAR UNA LINEA ARCHIVO *******************
# file_datos = open("datos_personales.txt", "a")
# file_datos.write("\nMasculino")
# file_datos.close()

# ************** LEER Y ESCRIBIR UN ARCHIVO *******************
# file_datos = open("datos_personales.txt", "r+")
# content = file_datos.read()
# print(content)
# file_datos.write("\nfcpulache8@zegelipae.pe")
# file_datos.write("\nZEGEL IPAE")
# file_datos.close()

# Sistema de Venta de pasajes
