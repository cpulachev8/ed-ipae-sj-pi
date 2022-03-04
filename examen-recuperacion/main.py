from Country import Country
from datetime import datetime

def add_country():
    name = input("Nombre: ")
    time_zone = input("Zona Horaria: ")
    countries.append(Country(name, time_zone, current_date=None))

def calculate_current_date():
    for c in countries:
        c.calculate_current_date(
            basic_country.get_sign_time_zone(),
            basic_country.get_number_hours_time_zone(),
            basic_country.current_date)

def print_countries():
    for c in countries:
        c.print()

# Agregando los 3 países
print("*** INGRESANDO 3 PAÍSES")
countries = []
print("PAÍS N° 1")
add_country()
print("PAÍS N° 2")
add_country()
print("PAÍS N° 3")
add_country()

# Ingresando país base
print("**** PAÍS BASE ***")
name = input("Nombre: ")
time_zone = input("Zona Horaria: ")
current_date = input("Fecha Actual: ")
basic_country = Country("Perú", "GMT-5", datetime.strptime(current_date, '%d/%m/%Y %I:%M %p'))

# Calculando fecha actual
calculate_current_date()

# Mostrar los países
print_countries()