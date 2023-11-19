import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProductosWindow(object):
    def setupUi(self, ProductosWindow):
        ProductosWindow.setObjectName("ProductosWindow")
        ProductosWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ProductosWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Pestañas para Fertilizantes y Controles de Plagas
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 760, 560))

        # Pestaña de Fertilizantes
        self.tabFertilizantes = QtWidgets.QWidget()
        self.tabFertilizantes.setObjectName("tabFertilizantes")
        self.setupFertilizantesTab(self.tabFertilizantes)
        self.tabWidget.addTab(self.tabFertilizantes, "Fertilizantes")

        # Pestaña de Controles de Plagas
        self.tabControlesPlagas = QtWidgets.QWidget()
        self.tabControlesPlagas.setObjectName("tabControlesPlagas")
        self.setupControlesPlagasTab(self.tabControlesPlagas)
        self.tabWidget.addTab(self.tabControlesPlagas, "Controles de Plagas")

        ProductosWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(ProductosWindow)
        QtCore.QMetaObject.connectSlotsByName(ProductosWindow)

    def setupFertilizantesTab(self, tab):
        # Componentes para Fertilizantes
        self.nombreFertilizanteLineEdit = QtWidgets.QLineEdit(tab)
        self.nombreFertilizanteLineEdit.setGeometry(QtCore.QRect(20, 50, 200, 24))
        self.registroICAFertilizanteLineEdit = QtWidgets.QLineEdit(tab)
        self.registroICAFertilizanteLineEdit.setGeometry(QtCore.QRect(20, 90, 200, 24))
        self.fechaAplicacionFertilizanteDateEdit = QtWidgets.QDateEdit(tab)
        self.fechaAplicacionFertilizanteDateEdit.setGeometry(QtCore.QRect(20, 130, 200, 24))
        self.agregarFertilizanteButton = QtWidgets.QPushButton("Agregar", tab)
        self.agregarFertilizanteButton.setGeometry(QtCore.QRect(250, 50, 100, 24))
        self.editarFertilizanteButton = QtWidgets.QPushButton("Editar", tab)
        self.editarFertilizanteButton.setGeometry(QtCore.QRect(250, 90, 100, 24))
        self.eliminarFertilizanteButton = QtWidgets.QPushButton("Eliminar", tab)
        self.eliminarFertilizanteButton.setGeometry(QtCore.QRect(250, 130, 100, 24))
        self.fertilizantesTableWidget = QtWidgets.QTableWidget(tab)
        self.fertilizantesTableWidget.setGeometry(QtCore.QRect(380, 20, 360, 200))
        self.fertilizantesTableWidget.setColumnCount(3)  # Nombre, Registro ICA, Fecha de aplicación
        self.fertilizantesTableWidget.setHorizontalHeaderLabels(["Nombre", "Registro ICA", "Fecha de Aplicación"])

    def setupControlesPlagasTab(self, tab):
        # Componentes para Controles de Plagas
        self.nombreControlPlagasLineEdit = QtWidgets.QLineEdit(tab)
        self.nombreControlPlagasLineEdit.setGeometry(QtCore.QRect(20, 50, 200, 24))
        self.registroICAControlPlagasLineEdit = QtWidgets.QLineEdit(tab)
        self.registroICAControlPlagasLineEdit.setGeometry(QtCore.QRect(20, 90, 200, 24))
        self.periodoCarenciaControlPlagasLineEdit = QtWidgets.QLineEdit(tab)
        self.periodoCarenciaControlPlagasLineEdit.setGeometry(QtCore.QRect(20, 130, 200, 24))
        self.agregarControlPlagasButton = QtWidgets.QPushButton("Agregar", tab)
        self.agregarControlPlagasButton.setGeometry(QtCore.QRect(250, 50, 100, 24))
        self.editarControlPlagasButton = QtWidgets.QPushButton("Editar", tab)
        self.editarControlPlagasButton.setGeometry(QtCore.QRect(250, 90, 100, 24))
        self.eliminarControlPlagasButton = QtWidgets.QPushButton("Eliminar", tab)
        self.eliminarControlPlagasButton.setGeometry(QtCore.QRect(250, 130, 100, 24))
        self.controlesPlagasTableWidget = QtWidgets.QTableWidget(tab)
        self.controlesPlagasTableWidget.setGeometry(QtCore.QRect(380, 20, 360, 200))
        self.controlesPlagasTableWidget.setColumnCount(3)  # Nombre, Registro ICA, Periodo de Carencia
        self.controlesPlagasTableWidget.setHorizontalHeaderLabels(["Nombre", "Registro ICA", "Periodo de Carencia"])

    def retranslateUi(self, ProductosWindow):
        _translate = QtCore.QCoreApplication.translate
        ProductosWindow.setWindowTitle(_translate("ProductosWindow", "Gestión de Productos"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ProductosWindow = QtWidgets.QMainWindow()
    ui = Ui_ProductosWindow()
    ui.setupUi(ProductosWindow)
    ProductosWindow.show()
    sys.exit(app.exec_())
