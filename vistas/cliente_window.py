import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClienteWindow(object):
    def setupUi(self, ClienteWindow):
        ClienteWindow.setObjectName("ClienteWindow")
        ClienteWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(ClienteWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Etiqueta y Campo de texto para el nombre del cliente
        self.label_nombre = QtWidgets.QLabel(self.centralwidget)
        self.label_nombre.setGeometry(QtCore.QRect(50, 20, 60, 16))
        self.label_nombre.setText("Nombre:")
        self.text_nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.text_nombre.setGeometry(QtCore.QRect(120, 20, 200, 22))

        # Etiqueta y Campo de texto para la cédula del cliente
        self.label_cedula = QtWidgets.QLabel(self.centralwidget)
        self.label_cedula.setGeometry(QtCore.QRect(50, 60, 60, 16))
        self.label_cedula.setText("Cédula:")
        self.text_cedula = QtWidgets.QLineEdit(self.centralwidget)
        self.text_cedula.setGeometry(QtCore.QRect(120, 60, 200, 22))

        # Botones para las acciones
        self.button_guardar = QtWidgets.QPushButton(self.centralwidget)
        self.button_guardar.setGeometry(QtCore.QRect(340, 20, 90, 28))
        self.button_guardar.setText("Guardar")
        
        self.button_editar = QtWidgets.QPushButton(self.centralwidget)
        self.button_editar.setGeometry(QtCore.QRect(340, 60, 90, 28))
        self.button_editar.setText("Editar")
        self.button_eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.button_eliminar.setGeometry(QtCore.QRect(440, 60, 90, 28))
        self.button_eliminar.setText("Eliminar")

        # Campo de entrada y botón para buscar por cédula
        self.label_buscar = QtWidgets.QLabel(self.centralwidget)
        self.label_buscar.setGeometry(QtCore.QRect(50, 300, 100, 16))
        self.label_buscar.setText("Buscar Cédula:")
        self.text_buscar = QtWidgets.QLineEdit(self.centralwidget)
        self.text_buscar.setGeometry(QtCore.QRect(160, 300, 160, 22))
        self.button_buscar = QtWidgets.QPushButton(self.centralwidget)
        self.button_buscar.setGeometry(QtCore.QRect(330, 300, 90, 28))
        self.button_buscar.setText("Buscar")

        # Conectar el botón de búsqueda con la función de búsqueda
        self.button_buscar.clicked.connect(self.buscar_cliente_por_cedula)

        # Tabla para mostrar los clientes
        self.table_clientes = QtWidgets.QTableWidget(self.centralwidget)
        self.table_clientes.setGeometry(QtCore.QRect(50, 100, 480, 192))
        self.table_clientes.setColumnCount(2)
        self.table_clientes.setHorizontalHeaderLabels(["Nombre", "Cédula"])

        ClienteWindow.setCentralWidget(self.centralwidget)

    def buscar_cliente_por_cedula(self):
        cedula = self.text_buscar.text()
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ClienteWindow = QtWidgets.QMainWindow()
    ui = Ui_ClienteWindow()
    ui.setupUi(ClienteWindow)
    ClienteWindow.show()
    sys.exit(app.exec_())
