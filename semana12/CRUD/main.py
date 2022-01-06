# CRUD: Create, Read, Update y Delete
# ABM: Altas, Bajas y Modificaciones
# Patrones de diseño (Leer para entrevistas)
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PyQt5.uic.uiparser import QtWidgets

from entities.Persona import Persona

def getPersons():
    persons = []
    persons.append(Persona("PER01", "José Romero", "09494832", "Peruana"))
    persons.append(Persona("PER02", "Diana Velarde", "64727373", "Chilena"))
    persons.append(Persona("PER03", "Ángel López", "93498321", "Venezolana"))
    persons.append(Persona("PER04", "David Casas", "43293902", "Ecuatoriana"))
    persons.append(Persona("PER05", "Bertha Castillo", "43293902", "Ecuatoriana"))
    persons.append(Persona("PER06", "Rosa Valdez", "43293902", "Ecuatoriana"))
    return persons

def crear_tabla():
    persons = getPersons()
    form_main.twPersonas.setRowCount(len(persons))
    # form_main.twPersonas.setColumnCount(4)    
    for i in range(len(persons)):
        form_main.twPersonas.setItem(i, 0, QTableWidgetItem(persons[i].id))
        form_main.twPersonas.setItem(i, 1, QTableWidgetItem(persons[i].dni))
        form_main.twPersonas.setItem(i, 2, QTableWidgetItem(persons[i].nombre))
        form_main.twPersonas.setItem(i, 3, QTableWidgetItem(persons[i].nacionalidad))

ui_path = os.path.dirname(os.path.abspath(__file__))
Form, Window = uic.loadUiType(os.path.join(ui_path, "ui", "crud-main.ui"))

app_crud = QApplication([])
window_main = Window()
form_main = Form()
form_main.setupUi(window_main)
window_main.show()
crear_tabla()
app_crud.exec()