from PyQt5 import QtCore, QtGui, QtWidgets
from controladores.clientes_controller import ClienteController
from controladores.factura_controller import FacturaController


class Ui_FacturaWindow(object):
    def setupUi(self, FacturaWindow):
        FacturaWindow.setObjectName("FacturaWindow")
        FacturaWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(FacturaWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Dropdown para seleccionar cliente
        self.label_cliente = QtWidgets.QLabel(self.centralwidget)
        self.label_cliente.setGeometry(QtCore.QRect(50, 20, 100, 20))
        self.label_cliente.setText("Cliente:")
        self.combo_cliente = QtWidgets.QComboBox(self.centralwidget)
        self.combo_cliente.setGeometry(QtCore.QRect(150, 20, 200, 22))

        # Campo para mostrar la fecha
        self.label_fecha = QtWidgets.QLabel(self.centralwidget)
        self.label_fecha.setGeometry(QtCore.QRect(50, 60, 100, 20))
        self.label_fecha.setText("Fecha:")
        self.date_fecha = QtWidgets.QDateEdit(self.centralwidget)
        self.date_fecha.setGeometry(QtCore.QRect(150, 60, 200, 22))
        self.date_fecha.setDateTime(QtCore.QDateTime.currentDateTime())

        # Tabla para productos
        self.table_productos = QtWidgets.QTableWidget(self.centralwidget)
        self.table_productos.setGeometry(QtCore.QRect(50, 100, 700, 300))
        self.table_productos.setColumnCount(3)
        self.table_productos.setHorizontalHeaderLabels(["Tipo", "Nombre", "Valor"])

        # Botón para agregar producto
        self.button_agregar_producto = QtWidgets.QPushButton(self.centralwidget)
        self.button_agregar_producto.setGeometry(QtCore.QRect(50, 420, 150, 30))
        self.button_agregar_producto.setText("Agregar Producto")

        # Botón para eliminar producto
        self.button_eliminar_producto = QtWidgets.QPushButton(self.centralwidget)
        self.button_eliminar_producto.setGeometry(QtCore.QRect(220, 420, 150, 30))
        self.button_eliminar_producto.setText("Eliminar Producto")

        # Botones para acciones de factura
        self.button_crear_factura = QtWidgets.QPushButton(self.centralwidget)
        self.button_crear_factura.setGeometry(QtCore.QRect(50, 470, 150, 30))
        self.button_crear_factura.setText("Crear Factura")

        self.button_guardar_cambios = QtWidgets.QPushButton(self.centralwidget)
        self.button_guardar_cambios.setGeometry(QtCore.QRect(220, 470, 150, 30))
        self.button_guardar_cambios.setText("Guardar Cambios")

        self.button_eliminar_factura = QtWidgets.QPushButton(self.centralwidget)
        self.button_eliminar_factura.setGeometry(QtCore.QRect(390, 470, 150, 30))
        self.button_eliminar_factura.setText("Eliminar Factura")

        FacturaWindow.setCentralWidget(self.centralwidget)

        self.clienteController = ClienteController()
        self.facturaController = FacturaController()

        # Cargar clientes cuando se inicia la ventana
        self.cargar_clientes()

        # Conectar botones a sus funciones correspondientes
        self.button_agregar_producto.clicked.connect(self.agregar_producto)
        self.button_eliminar_producto.clicked.connect(self.eliminar_producto)
        self.button_crear_factura.clicked.connect(self.crear_factura)
        self.button_guardar_cambios.clicked.connect(self.guardar_cambios_factura)
        self.button_eliminar_factura.clicked.connect(self.eliminar_factura)

    def cargar_clientes(self):
        clientes = self.clienteController.obtener_todos_los_clientes()
        for cliente in clientes:
            self.combo_cliente.addItem(cliente.nombre, cliente.id)

    def agregar_producto(self):
        producto_id = self.obtener_id_producto_seleccionado()
        factura_id = self.obtener_id_factura_actual()
        es_antibiotico = self.es_producto_antibiotico(producto_id)

        try:
            self.facturaController.agregar_producto_a_factura(factura_id, producto_id, es_antibiotico)
            self.actualizar_tabla_productos(factura_id)  # Actualizar la tabla de productos
        except Exception as e:
            self.mostrar_mensaje_error(str(e))

    def obtener_id_producto_seleccionado(self):
        nombre_producto_seleccionado = self.dropdown_productos.currentText()
        producto = self.productoController.obtener_producto_por_nombre(nombre_producto_seleccionado)
        return producto.id if producto else None

    def obtener_id_factura_actual(self):
        return self.factura_actual_id

    def es_producto_antibiotico(self, producto_id):
        return self.productoController.es_producto_antibiotico(producto_id)

    def guardar_cambios_factura(self):
        factura_id = self.obtener_id_factura_actual()
        if factura_id is None:
            self.mostrar_mensaje_error("No se ha seleccionado ninguna factura")
            return

        try:
            cliente_id = self.combo_cliente.currentData()
            productos = self.obtener_productos_actualizados()

            self.facturaController.actualizar_factura(factura_id, cliente_id, productos)

        except Exception as e:
            self.mostrar_mensaje_error(str(e))


def eliminar_factura(self):
    factura_id = self.obtener_id_factura_actual()
    if factura_id is None:
        self.mostrar_mensaje_error("No se ha seleccionado ninguna factura")
        return

    try:
        self.facturaController.eliminar_factura(factura_id)
        # Aquí podrías actualizar la UI para reflejar que la factura ha sido eliminada
    except Exception as e:
        self.mostrar_mensaje_error(str(e))


def mostrar_mensaje_error(self, mensaje):
    QtWidgets.QMessageBox.critical(None, "Error", mensaje)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    FacturaWindow = QtWidgets.QMainWindow()
    ui = Ui_FacturaWindow()
    ui.setupUi(FacturaWindow)
    FacturaWindow.show()
    sys.exit(app.exec_())
