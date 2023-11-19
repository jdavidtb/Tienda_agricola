from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FacturaWindow(object):
    def setupUi(self, FacturaWindow):
        FacturaWindow.setObjectName("FacturaWindow")
        FacturaWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(FacturaWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Etiqueta para la fecha
        self.label_fecha = QtWidgets.QLabel(self.centralwidget)
        self.label_fecha.setGeometry(QtCore.QRect(50, 20, 60, 16))

        # Selector de fecha (QDateEdit)
        self.date_fecha = QtWidgets.QDateEdit(self.centralwidget)
        self.date_fecha.setGeometry(QtCore.QRect(120, 20, 110, 22))

        # Etiqueta para el valor total
        self.label_valor_total = QtWidgets.QLabel(self.centralwidget)
        self.label_valor_total.setGeometry(QtCore.QRect(240, 20, 70, 16))

        # Campo de texto para el valor total
        self.text_valor_total = QtWidgets.QLineEdit(self.centralwidget)
        self.text_valor_total.setGeometry(QtCore.QRect(320, 20, 110, 22))

        # Etiqueta para la cédula del cliente
        self.label_cedula_cliente = QtWidgets.QLabel(self.centralwidget)
        self.label_cedula_cliente.setGeometry(QtCore.QRect(440, 20, 50, 16))

        # Campo de texto para la cédula del cliente
        self.text_cedula_cliente = QtWidgets.QLineEdit(self.centralwidget)
        self.text_cedula_cliente.setGeometry(QtCore.QRect(500, 20, 110, 22))

        # Lista desplegable para seleccionar productos
        self.combo_productos = QtWidgets.QComboBox(self.centralwidget)
        self.combo_productos.setGeometry(QtCore.QRect(50, 60, 200, 22))

        # Botón para añadir productos a la factura
        self.button_add_producto = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_producto.setGeometry(QtCore.QRect(260, 60, 90, 28))

        # Botón para finalizar la venta
        self.button_finalizar_venta = QtWidgets.QPushButton(self.centralwidget)
        self.button_finalizar_venta.setGeometry(QtCore.QRect(360, 60, 90, 28))

        # Tabla para mostrar los productos añadidos a la factura
        self.table_productos_factura = QtWidgets.QTableWidget(self.centralwidget)
        self.table_productos_factura.setGeometry(QtCore.QRect(50, 100, 700, 400))
        self.table_productos_factura.setColumnCount(4)  # Por ejemplo, ID, Nombre, Cantidad, Precio
        self.table_productos_factura.setHorizontalHeaderLabels(["ID", "Nombre", "Cantidad", "Precio"])

        FacturaWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FacturaWindow)
        QtCore.QMetaObject.connectSlotsByName(FacturaWindow)

    def retranslateUi(self, FacturaWindow):
        _translate = QtCore.QCoreApplication.translate
        FacturaWindow.setWindowTitle(_translate("FacturaWindow", "Gestión de Facturas"))
        self.label_fecha.setText(_translate("FacturaWindow", "Fecha:"))
        self.label_valor_total.setText(_translate("FacturaWindow", "Valor Total:"))
        self.label_cedula_cliente.setText(_translate("FacturaWindow", "Cédula:"))
        self.button_add_producto.setText(_translate("FacturaWindow", "Añadir"))
        self.button_finalizar_venta.setText(_translate("FacturaWindow", "Finalizar Venta"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FacturaWindow = QtWidgets.QMainWindow()
    ui = Ui_FacturaWindow()
    ui.setupUi(FacturaWindow)
    FacturaWindow.show()
    sys.exit(app.exec_())
