from PyQt5 import QtWidgets
from vistas.main_window   import Ui_MainWindow
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)  # Crea la aplicación

    # Configura la ventana principal
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()  # Muestra la ventana principal

    sys.exit(app.exec_())  # Inicia el bucle de eventos

if __name__ == "__main__":
    main()
