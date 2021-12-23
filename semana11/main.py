from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog

class DialogWelcome(QDialog):

    def __init__(self) -> None:
        super(DialogWelcome, self).__init__()
        uic.loadUi("mi-primer-dialog.ui", self)
        self.lbWelcome.setText("Bienvenido {}".format(form_gui.leUser.text()))

def start():
    print("Click en el botón iniciar", form_gui.leUser.text())
    dialogWelcome = DialogWelcome()
    dialogWelcome.exec()

Form, Window = uic.loadUiType("mi-primer-gui.ui")

app_gui = QApplication([])
window_gui = Window()
form_gui = Form()
form_gui.setupUi(window_gui)
window_gui.show()
form_gui.pbStart.clicked.connect(start)
app_gui.exec()