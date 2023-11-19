from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AntibioticosWindow(object):
    def setupUi(self, AntibioticosWindow):
        AntibioticosWindow.setObjectName("AntibioticosWindow")
        AntibioticosWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AntibioticosWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Etiqueta y campo de texto para la Dosis
        self.label_dosis = QtWidgets.QLabel(self.centralwidget)
        self.label_dosis.setGeometry(QtCore.QRect(50, 20, 100, 16))
        self.text_dosis = QtWidgets.QLineEdit(self.centralwidget)
        self.text_dosis.setGeometry(QtCore.QRect(160, 20, 200, 22))

        # Etiqueta y campo de texto para el Tipo de Animal
        self.label_tipo_animal = QtWidgets.QLabel(self.centralwidget)
        self.label_tipo_animal.setGeometry(QtCore.QRect(50, 50, 150, 16))
        self.text_tipo_animal = QtWidgets.QLineEdit(self.centralwidget)
        self.text_tipo_animal.setGeometry(QtCore.QRect(160, 50, 200, 22))

        # Etiqueta y campo de texto para el ID del Antibiótico
        self.label_id_antibiotico = QtWidgets.QLabel(self.centralwidget)
        self.label_id_antibiotico.setGeometry(QtCore.QRect(50, 80, 100, 16))
        self.text_id_antibiotico = QtWidgets.QLineEdit(self.centralwidget)
        self.text_id_antibiotico.setGeometry(QtCore.QRect(160, 80, 200, 22))

        # Etiqueta y campo de texto para el Nombre del Antibiótico
        self.label_nombre_antibiotico = QtWidgets.QLabel(self.centralwidget)
        self.label_nombre_antibiotico.setGeometry(QtCore.QRect(50, 110, 100, 16))
        self.text_nombre_antibiotico = QtWidgets.QLineEdit(self.centralwidget)
        self.text_nombre_antibiotico.setGeometry(QtCore.QRect(160, 110, 200, 22))

        # Etiqueta y campo de texto para el Valor del Antibiótico
        self.label_valor_antibiotico = QtWidgets.QLabel(self.centralwidget)
        self.label_valor_antibiotico.setGeometry(QtCore.QRect(50, 140, 100, 16))
        self.text_valor_antibiotico = QtWidgets.QLineEdit(self.centralwidget)
        self.text_valor_antibiotico.setGeometry(QtCore.QRect(160, 140, 200, 22))

        # Botones para Guardar, Editar y Eliminar
        self.button_guardar = QtWidgets.QPushButton("Guardar", self.centralwidget)
        self.button_guardar.setGeometry(QtCore.QRect(380, 20, 90, 28))
        self.button_editar = QtWidgets.QPushButton("Editar", self.centralwidget)
        self.button_editar.setGeometry(QtCore.QRect(380, 50, 90, 28))
        self.button_eliminar = QtWidgets.QPushButton("Eliminar", self.centralwidget)
        self.button_eliminar.setGeometry(QtCore.QRect(380, 80, 90, 28))

        # Tabla para mostrar los antibióticos existentes
        self.table_antibioticos = QtWidgets.QTableWidget(self.centralwidget)
        self.table_antibioticos.setGeometry(QtCore.QRect(50, 180, 700, 300))
        self.table_antibioticos.setColumnCount(5)  # Por ejemplo, ID, Nombre, Dosis, Tipo de Animal, Valor
        self.table_antibioticos.setHorizontalHeaderLabels(["ID", "Nombre", "Dosis", "Tipo de Animal", "Valor"])

        AntibioticosWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AntibioticosWindow)
        QtCore.QMetaObject.connectSlotsByName(AntibioticosWindow)

    def retranslateUi(self, AntibioticosWindow):
        _translate = QtCore.QCoreApplication.translate
        AntibioticosWindow.setWindowTitle(_translate("AntibioticosWindow", "Gestión de Antibióticos"))
        self.label_dosis.setText(_translate("AntibioticosWindow", "Dosis:"))
        self.label_tipo_animal.setText(_translate("AntibioticosWindow", "Tipo de Animal:"))
        self.label_id_antibiotico.setText(_translate("AntibioticosWindow", "ID Antibiótico:"))
        self.label_nombre_antibiotico.setText(_translate("AntibioticosWindow", "Nombre Antibiótico:"))
        self.label_valor_antibiotico.setText(_translate("AntibioticosWindow", "Valor:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AntibioticosWindow = QtWidgets.QMainWindow()
    ui = Ui_AntibioticosWindow()
    ui.setupUi(AntibioticosWindow)
    AntibioticosWindow.show()
    sys.exit(app.exec_())