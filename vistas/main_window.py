from PyQt5 import QtCore, QtGui, QtWidgets
from antibioticos_window import Ui_AntibioticosWindow
from factura_window import Ui_FacturaWindow
from cliente_window import Ui_ClienteWindow
from producto_window import Ui_ProductosWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Título de la Aplicación
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(200, 10, 400, 60))  # Ajusta la posición y tamaño según necesites
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setText("Tienda Agrícola")
        self.titleLabel.setObjectName("titleLabel")

        # Grupo Principal
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 80, 661, 351))
        self.groupBox.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.groupBox.setObjectName("groupBox")

        # Botones y Etiquetas
        self.setupButtonsAndLabels()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #Abrir las ventanas deseadas
        self.pushButton.clicked.connect(self.abrirVentanaClientes)
        self.pushButton_2.clicked.connect(self.abrirVentanaFacturas)
        self.pushButton_3.clicked.connect(self.abrirVentanaProductos)
        self.pushButton_4.clicked.connect(self.abrirVentanaAntibioticos)

    def abrirVentanaClientes(self):
        self.ventanaClientes = QtWidgets.QMainWindow()
        ui = Ui_ClienteWindow()
        ui.setupUi(self.ventanaClientes)
        self.ventanaClientes.show()

    def abrirVentanaProductos(self):
        self.ventanaProductos = QtWidgets.QMainWindow()
        ui = Ui_ProductosWindow()
        ui.setupUi(self.ventanaProductos)
        self.ventanaProductos.show()
    def abrirVentanaFacturas(self):
        self.ventanaFacturas= QtWidgets.QMainWindow()
        ui=Ui_FacturaWindow()
        ui.setupUi(self.ventanaFacturas)
        self.ventanaFacturas.show()
    def abrirVentanaAntibioticos(self):
        self.ventanaAntibioticos=QtWidgets.QMainWindow()
        ui= Ui_AntibioticosWindow()
        ui.setupUi(self.ventanaAntibioticos)
        self.ventanaAntibioticos.show()
    def setupButtonsAndLabels(self):
        # Configuración de botones y etiquetas
        font = QtGui.QFont()
        font.setPointSize(12)

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(30, 90, 241, 23))
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 140, 241, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 90, 261, 23))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 150, 251, 23))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tienda Agrícola"))
        self.pushButton.setText(_translate("MainWindow", "Gestionar Clientes"))
        self.pushButton_2.setText(_translate("MainWindow", "Crear Factura"))
        self.pushButton_3.setText(_translate("MainWindow", "Gestionar Productos de Control"))
        self.pushButton_4.setText(_translate("MainWindow", "Gestionar Antibióticos"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
