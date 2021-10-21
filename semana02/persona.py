def ingreso():
    nombre = input("Ingrese Nombre: ")
    dni = input("Ingrese DNI: ")
    celular = input("Ingrese Celular: ")

    return {"nombre": nombre, "dni": dni, "celular": celular}

def ver_datos(nombre, dni):
    return "La persona %s con DNI %s"%(nombre, dni)