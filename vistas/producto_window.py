import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from controladores.control_fertilizantesController import ControlDeFertilizantesController
from controladores.control_plagasController import ControlDePlagasController


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

        self.fertilizanteController = ControlDeFertilizantesController()
        self.plagasController = ControlDePlagasController()
        # Conectar botones
        self.agregarFertilizanteButton.clicked.connect(self.agregar_fertilizante)
        self.editarControlPlagasButton.clicked.connect(self.editar_fertilizante)
        self.eliminarControlPlagasButton.clicked.connect(self.eliminar_fertilizante)
        self.agregarControlPlagasButton.clicked.connect(self.agregar_control_plagas)
        self.editarControlPlagasButton.clicked.connect(self.editar_control_plagas)
        self.eliminarControlPlagasButton.clicked.connect(self.eliminar_control_plagas)

    def agregar_fertilizante(self):
        nombre = self.nombreFertilizanteLineEdit.text()
        registro_ica = self.registroICAFertilizanteLineEdit.text()
        fecha_aplicacion = self.fechaAplicacionFertilizanteDateEdit.date().toString("yyyy-MM-dd")
        valor = ...  # Obtener el valor

        try:
            self.fertilizanteController.crear_fertilizante(nombre, registro_ica, "frecuencia", valor, fecha_aplicacion)
            # Actualizar tabla
            self.cargar_fertilizantes()
        except Exception as e:
            self.mostrar_mensaje_error(str(e))

    def editar_fertilizante(self):
        selected_items = self.fertilizantesTableWidget.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            fertilizante_id = self.fertilizantesTableWidget.item(row, 0).data(QtCore.Qt.UserRole)
            nombre = self.nombreFertilizanteLineEdit.text()
            registro_ica = self.registroICAFertilizanteLineEdit.text()
            fecha_aplicacion = self.fechaAplicacionFertilizanteDateEdit.date().toString("yyyy-MM-dd")
            valor = self.valorFertilizanteLineEdit.text()  # Aquí leemos el valor del QLineEdit

            try:
                # Asegúrate de que los tipos de datos coincidan con lo que espera tu controlador y base de datos
                valor = float(valor)  # Convierte a float si el valor es un número decimal
                self.fertilizanteController.actualizar_fertilizante(fertilizante_id, nombre=nombre,
                                                                    registro_ica=registro_ica,
                                                                    fecha_ultima_aplicacion=fecha_aplicacion,
                                                                    valor=valor)
                self.cargar_fertilizantes()
            except Exception as e:
                self.mostrar_mensaje_error(str(e))
        else:
            self.mostrar_mensaje_error("Selecciona un fertilizante para editar")

    def eliminar_fertilizante(self):
        selected_items = self.fertilizantesTableWidget.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            fertilizante_id = self.fertilizantesTableWidget.item(row, 0).data(QtCore.Qt.UserRole)

            try:
                self.fertilizanteController.eliminar_fertilizante(fertilizante_id)
                self.cargar_fertilizantes()
            except Exception as e:
                self.mostrar_mensaje_error(str(e))
        else:
            self.mostrar_mensaje_error("Selecciona un fertilizante para eliminar")

    def mostrar_mensaje_error(self, mensaje):
        QtWidgets.QMessageBox.critical(None, "Error", mensaje)

    def agregar_control_plagas(self):
        nombre = self.nombreControlPlagasLineEdit.text()
        registro_ica = self.registroICAControlPlagasLineEdit.text()
        periodo_carencia = self.periodoCarenciaControlPlagasLineEdit.text()
        valor = ...  # Obtener el valor

        try:
            self.plagasController.crear_control_plagas(nombre, registro_ica, "frecuencia", valor, periodo_carencia)
            self.cargar_controles_plagas()
        except Exception as e:
            self.mostrar_mensaje_error(str(e))

    def editar_control_plagas(self):
        selected_items = self.controlesPlagasTableWidget.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            control_plagas_id = self.controlesPlagasTableWidget.item(row, 0).data(QtCore.Qt.UserRole)
            nombre = self.nombreControlPlagasLineEdit.text()
            registro_ica = self.registroICAControlPlagasLineEdit.text()
            periodo_carencia = self.periodoCarenciaControlPlagasLineEdit.text()

            try:
                self.plagasController.actualizar_control_plagas(control_plagas_id, nombre=nombre,
                                                                registro_ica=registro_ica,
                                                                periodo_carencia=periodo_carencia, valor=valor)
                self.cargar_controles_plagas()
            except Exception as e:
                self.mostrar_mensaje_error(str(e))
        else:
            self.mostrar_mensaje_error("Selecciona un control de plagas para editar")

    def eliminar_control_plagas(self):
        selected_items = self.controlesPlagasTableWidget.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            control_plagas_id = self.controlesPlagasTableWidget.item(row, 0).data(QtCore.Qt.UserRole)

            try:
                self.plagasController.eliminar_control_plagas(control_plagas_id)
                self.cargar_controles_plagas()
            except Exception as e:
                self.mostrar_mensaje_error(str(e))
        else:
            self.mostrar_mensaje_error("Selecciona un control de plagas para eliminar")

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
