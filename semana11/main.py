from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

def start():
    print("Click en el botón iniciar", form_gui.leUser.text())

Form, Window = uic.loadUiType("mi-primer-gui.ui")

app_gui = QApplication([])
window_gui = Window()
form_gui = Form()
form_gui.setupUi(window_gui)
window_gui.show()
form_gui.pbStart.clicked.connect(start)
app_gui.exec()