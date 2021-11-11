# El identificador de clase es la palabra class 
# Es una clase vacía
class Alumno:
    pass # Se usa para definir una clase vacía

# Es una clase con atributos por defecto
class Persona:
    nombre = "Pedro"
    edad = 20
    sexo = "Masculino"

# Es una clase con un método de inicialización que permite iniciar atributos con valores diferentes
class Vehiculo:    

    def __init__(self, marca, anio_fabricacion):
        self.marca = marca
        self.anio_fabricacion = anio_fabricacion
    
    def mostrar_datos(self):
        print("Es un vehículo de la marca {}, con año de fabricación {}".format(self.marca, self.anio_fabricacion))


# Crear un objeto de la clase persona - instanciar
pedro = "Es un persona"
juan = Persona()

print(pedro)
print("Nombre: {}, edad: {}, sexo: {}".format(juan.nombre, juan.edad, juan.sexo))

# Creación de 2 objetos de la clase vehículo
veh1 = Vehiculo("Toyota", 2010)
veh2 = Vehiculo("Kia", 2019)

# Se está invocando el método mostrar_datos() de los vehículos creados
veh1.mostrar_datos()
veh2.mostrar_datos()