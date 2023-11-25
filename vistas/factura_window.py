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
        except Exception as e:
            self.mostrar_mensaje_error(str(e))


    def eliminar_producto(self):
            selected_items = self.table_productos.selectedItems()
            if selected_items:
                row = selected_items[0].row()  # Obtiene la fila del producto seleccionado

                # Suponemos que tienes el ID del producto almacenado en la tabla
                producto_id = self.table_productos.item(row, 0).text()  # Ajusta el índice de la columna según corresponda

                # Suponemos que necesitas el ID de la factura actual
                factura_id = self.obtener_id_factura_actual()  # Asegúrate de que esta función devuelva el ID correcto

                # Llamada al método del controlador para eliminar el producto de la factura
                try:
                    self.facturaController.eliminar_producto_de_factura(factura_id, producto_id)
                    self.table_productos.removeRow(row)  # Elimina la fila de la tabla
                except Exception as e:
                    self.mostrar_mensaje_error(str(e))
            else:
                self.mostrar_mensaje_error("Selecciona un producto para eliminar")

    def obtener_id_cliente_seleccionado(self):
        return self.combo_cliente.currentData()

    def crear_factura(self):
        cliente_id = self.obtener_id_cliente_seleccionado()
        if cliente_id is not None:
            try:
                nueva_factura = self.facturaController.crear_factura(cliente_id)
                # Aquí puedes manejar lo que sucede después de crear la factura
                # Por ejemplo, mostrar un mensaje de éxito, actualizar una lista de facturas, etc.
                self.mostrar_mensaje_exito(f"Factura creada con éxito. ID de factura: {nueva_factura.id}")
            except Exception as e:
                self.mostrar_mensaje_error(f"Error al crear factura: {e}")
        else:
            self.mostrar_mensaje_error("Selecciona un cliente para crear la factura")

    def mostrar_mensaje_exito(self, mensaje):
        QtWidgets.QMessageBox.information(None, "Éxito", mensaje)

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
