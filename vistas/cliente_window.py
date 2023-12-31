import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from controladores.clientes_controller import ClienteController
from PyQt5.QtCore import Qt


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
        self.clienteController = ClienteController()
        # Conectar botones con las funciones
        QtCore.QMetaObject.connectSlotsByName(ClienteWindow)
        self.button_guardar.clicked.connect(self.metodo_prueba)
        self.button_editar.clicked.connect(self.editar_cliente)
        self.button_eliminar.clicked.connect(self.eliminar_cliente)
        self.button_buscar.clicked.connect(self.buscar_cliente_por_cedula)
        # Actualizar la lista de clientes al iniciar
        self.cargar_clientes()

    # Funciones conectadas a los botones
    def guardar_cliente(self):
        print("Guardando cliente...")
        nombre = self.text_nombre.text().strip()
        cedula = self.text_cedula.text().strip()
        print(f"Guardando cliente: Nombre={nombre}, Cedula={cedula}")
        if nombre and cedula:  # Asegúrate de que ambos campos estén llenos
            try:
                self.clienteController.crear_cliente(nombre, cedula)
                self.actualizar_tabla_clientes()  # Llamada a la función para actualizar la tabla
                QtWidgets.QMessageBox.information(None, "Éxito", "Cliente guardado con éxito.")
                self.text_nombre.clear()  # Limpia el campo del nombre
                self.text_cedula.clear()  # Limpia el campo de la cédula
            except Exception as e:
                QtWidgets.QMessageBox.critical(None, "Error", f"Error al guardar el cliente: {e}")
        else:
            QtWidgets.QMessageBox.warning(None, "Advertencia", "Nombre y cédula son requeridos.")

    def actualizar_tabla_clientes(self):
        print("Actualizando tabla de clientes...")
        self.table_clientes.setRowCount(0)  # Limpia la tabla
        clientes = self.clienteController.obtener_todos_los_clientes()
        for cliente in clientes:
            row_position = self.table_clientes.rowCount()
            self.table_clientes.insertRow(row_position)
            self.table_clientes.setItem(row_position, 0, QtWidgets.QTableWidgetItem(cliente.nombre))
            self.table_clientes.setItem(row_position, 1, QtWidgets.QTableWidgetItem(cliente.cedula))
            self.table_clientes.item(row_position, 0).setData(QtCore.Qt.UserRole, cliente.id)
    def editar_cliente(self):
        # Obtener el cliente seleccionado de la tabla
        selected_items = self.table_clientes.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            cliente_id = self.table_clientes.item(row, 0).data(QtCore.Qt.UserRole)
            nombre = self.text_nombre.text()
            cedula = self.text_cedula.text()
            self.clienteController.actualizar_cliente(cliente_id, nombre, cedula)
            self.cargar_clientes()

    def eliminar_cliente(self):
        selected_items = self.table_clientes.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            cliente_id = self.table_clientes.item(row, 0).data(QtCore.Qt.UserRole)
            self.clienteController.eliminar_cliente(cliente_id)
            self.cargar_clientes()

    def buscar_cliente_por_cedula(self):
        cedula = self.text_buscar.text()
        cliente = self.clienteController.obtener_cliente_por_cedula(cedula)
        if cliente:
            # Limpia la tabla y agrega el cliente encontrado
            self.table_clientes.clearContents()
            self.table_clientes.setRowCount(1)
            self.table_clientes.setItem(0, 0, QtWidgets.QTableWidgetItem(cliente.nombre))
            self.table_clientes.setItem(0, 1, QtWidgets.QTableWidgetItem(cliente.cedula))
            self.table_clientes.item(0, 0).setData(QtCore.Qt.UserRole, cliente.id)
        else:
            # Manejar el caso de no encontrar el cliente
            self.table_clientes.clearContents()
            self.table_clientes.setRowCount(0)
            QtWidgets.QMessageBox.information(None, 'Búsqueda', 'Cliente no encontrado.')

    def cargar_clientes(self):
        # Obtener todos los clientes y cargarlos en la tabla
        clientes = self.clienteController.obtener_todos_los_clientes()
        self.table_clientes.clearContents()
        self.table_clientes.setRowCount(len(clientes))
        for row_number, cliente in enumerate(clientes):
            self.table_clientes.setItem(row_number, 0, QtWidgets.QTableWidgetItem(cliente.nombre))
            self.table_clientes.setItem(row_number, 1, QtWidgets.QTableWidgetItem(cliente.cedula))
            self.table_clientes.item(row_number, 0).setData(QtCore.Qt.UserRole, cliente.id)

    def metodo_prueba(self):
        print("El botón ha sido presionado.")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ClienteWindow = QtWidgets.QMainWindow()
    ui = Ui_ClienteWindow()
    ui.setupUi(ClienteWindow)
    ClienteWindow.show()
    sys.exit(app.exec_())
