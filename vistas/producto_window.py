import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from controladores.control_fertilizantesController import ControlDeFertilizantesController
from controladores.control_plagasController import ControlDePlagasController

class Ui_ProductosControlWindow(object):
    def setupUi(self, ProductosControlWindow):
        ProductosControlWindow.setObjectName("ProductosControlWindow")
        ProductosControlWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ProductosControlWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 780, 580))
        self.tabWidget.setObjectName("tabWidget")

        self.setupTabPlagas()
        self.setupTabFertilizantes()

        ProductosControlWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ProductosControlWindow)
        self.statusbar.setObjectName("statusbar")
        ProductosControlWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ProductosControlWindow)
        QtCore.QMetaObject.connectSlotsByName(ProductosControlWindow)

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
        valor = self.valorControlPlagasLineEdit.text()

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
            valor = self.valorFertilizanteLineEdit.text()

            try:
                valor = float(valor)
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
        valor = self.valorControlPlagasLineEdit.text()

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
            valor = self.valorControlPlagasLineEdit.text()

            try:
                valor = float(valor)
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

    def setupTabPlagas(self):
        self.tabPlagas = QtWidgets.QWidget()
        self.tabPlagas.setObjectName("tabPlagas")

        self.label_nombre_ControlPlagas = QtWidgets.QLabel(self.tabPlagas)
        self.label_nombre_ControlPlagas.setText("Nombre:")
        self.label_nombre_ControlPlagas.setGeometry(QtCore.QRect(20, 20, 200, 24))

        self.label_registro_ica_ControlPlagas = QtWidgets.QLabel(self.tabPlagas)
        self.label_registro_ica_ControlPlagas.setText("Registro ICA:")
        self.label_registro_ica_ControlPlagas.setGeometry(QtCore.QRect(20, 60, 200, 24))

        self.label_fecha_aplicacion_ControlPlagas = QtWidgets.QLabel(self.tabPlagas)
        self.label_fecha_aplicacion_ControlPlagas.setText("Periodo de carencia:")
        self.label_fecha_aplicacion_ControlPlagas.setGeometry(QtCore.QRect(20, 100, 200, 24))

        self.label_valor_ControlPlagas = QtWidgets.QLabel(self.tabPlagas)
        self.label_valor_ControlPlagas.setText("Valor:")
        self.label_valor_ControlPlagas.setGeometry(QtCore.QRect(20, 140, 200, 24))

        self.nombreControlPlagasLineEdit = QtWidgets.QLineEdit(self.tabPlagas)
        self.nombreControlPlagasLineEdit.setGeometry(QtCore.QRect(100, 20, 200, 24))
        self.nombreControlPlagasLineEdit.setObjectName("nombreControlPlagasLineEdit")

        self.registroICAControlPlagasLineEdit = QtWidgets.QLineEdit(self.tabPlagas)
        self.registroICAControlPlagasLineEdit.setGeometry(QtCore.QRect(100, 60, 200, 24))
        self.registroICAControlPlagasLineEdit.setObjectName("registroICAControlPlagasLineEdit")

        self.periodoCarenciaControlPlagasLineEdit = QtWidgets.QLineEdit(self.tabPlagas)
        self.periodoCarenciaControlPlagasLineEdit.setGeometry(QtCore.QRect(120, 100, 200, 24))
        self.periodoCarenciaControlPlagasLineEdit.setObjectName("periodoCarenciaControlPlagasLineEdit")

        self.valorControlPlagasLineEdit = QtWidgets.QLineEdit(self.tabPlagas)
        self.valorControlPlagasLineEdit.setGeometry(QtCore.QRect(100, 140, 200, 24))
        self.valorControlPlagasLineEdit.setObjectName("valorControlPlagasLineEdit")

        self.agregarControlPlagasButton = QtWidgets.QPushButton(self.tabPlagas)
        self.agregarControlPlagasButton.setGeometry(QtCore.QRect(450, 20, 150, 24))
        self.agregarControlPlagasButton.setObjectName("agregarControlPlagasButton")

        self.editarControlPlagasButton = QtWidgets.QPushButton(self.tabPlagas)
        self.editarControlPlagasButton.setGeometry(QtCore.QRect(450, 60, 150, 24))
        self.editarControlPlagasButton.setObjectName("editarControlPlagasButton")

        self.eliminarControlPlagasButton = QtWidgets.QPushButton(self.tabPlagas)
        self.eliminarControlPlagasButton.setGeometry(QtCore.QRect(450, 100, 150, 24))
        self.eliminarControlPlagasButton.setObjectName("eliminarControlPlagasButton")

        self.controlesPlagasTableWidget = QtWidgets.QTableWidget(self.tabPlagas)
        self.controlesPlagasTableWidget.setGeometry(QtCore.QRect(20, 180, 740, 360))
        self.controlesPlagasTableWidget.setObjectName("controlesPlagasTableWidget")
        self.controlesPlagasTableWidget.setColumnCount(0)
        self.controlesPlagasTableWidget.setRowCount(0)

        self.tabWidget.addTab(self.tabPlagas, "Control de Plagas")

    def setupTabFertilizantes(self):
        self.tabFertilizantes = QtWidgets.QWidget()
        self.tabFertilizantes.setObjectName("tabFertilizantes")

        self.label_nombre_fertilizante = QtWidgets.QLabel(self.tabFertilizantes)
        self.label_nombre_fertilizante.setText("Nombre:")
        self.label_nombre_fertilizante.setGeometry(QtCore.QRect(20, 20, 200, 24))

        self.label_registro_ica_fertilizante = QtWidgets.QLabel(self.tabFertilizantes)
        self.label_registro_ica_fertilizante.setText("Registro ICA:")
        self.label_registro_ica_fertilizante.setGeometry(QtCore.QRect(20, 60, 200, 24))

        self.label_fecha_aplicacion_fertilizante = QtWidgets.QLabel(self.tabFertilizantes)
        self.label_fecha_aplicacion_fertilizante.setText("Fecha Última Aplicación:")
        self.label_fecha_aplicacion_fertilizante.setGeometry(QtCore.QRect(20, 100, 200, 24))

        self.label_valor_fertilizante = QtWidgets.QLabel(self.tabFertilizantes)
        self.label_valor_fertilizante.setText("Valor:")
        self.label_valor_fertilizante.setGeometry(QtCore.QRect(20, 140, 200, 24))

        self.nombreFertilizanteLineEdit = QtWidgets.QLineEdit(self.tabFertilizantes)
        self.nombreFertilizanteLineEdit.setGeometry(QtCore.QRect(100, 20, 200, 24))
        self.nombreFertilizanteLineEdit.setObjectName("nombreFertilizanteLineEdit")

        self.registroICAFertilizanteLineEdit = QtWidgets.QLineEdit(self.tabFertilizantes)
        self.registroICAFertilizanteLineEdit.setGeometry(QtCore.QRect(100, 60, 200, 24))
        self.registroICAFertilizanteLineEdit.setObjectName("registroICAFertilizanteLineEdit")

        self.fechaAplicacionFertilizanteDateEdit = QtWidgets.QDateEdit(self.tabFertilizantes)
        self.fechaAplicacionFertilizanteDateEdit.setGeometry(QtCore.QRect(145, 100, 200, 24))
        self.fechaAplicacionFertilizanteDateEdit.setObjectName("fechaAplicacionFertilizanteDateEdit")

        self.valorFertilizanteLineEdit = QtWidgets.QLineEdit(self.tabFertilizantes)
        self.valorFertilizanteLineEdit.setGeometry(QtCore.QRect(70, 140, 200, 24))
        self.valorFertilizanteLineEdit.setObjectName("valorFertilizanteLineEdit")

        self.agregarFertilizanteButton = QtWidgets.QPushButton(self.tabFertilizantes)
        self.agregarFertilizanteButton.setGeometry(QtCore.QRect(450, 20, 150, 24))
        self.agregarFertilizanteButton.setObjectName("agregarFertilizanteButton")

        self.editarFertilizanteButton = QtWidgets.QPushButton(self.tabFertilizantes)
        self.editarFertilizanteButton.setGeometry(QtCore.QRect(450, 60, 150, 24))
        self.editarFertilizanteButton.setObjectName("editarFertilizanteButton")

        self.eliminarFertilizanteButton = QtWidgets.QPushButton(self.tabFertilizantes)
        self.eliminarFertilizanteButton.setGeometry(QtCore.QRect(450, 100, 150, 24))
        self.eliminarFertilizanteButton.setObjectName("eliminarFertilizanteButton")

        self.fertilizantesTableWidget = QtWidgets.QTableWidget(self.tabFertilizantes)
        self.fertilizantesTableWidget.setGeometry(QtCore.QRect(20, 180, 740, 360))
        self.fertilizantesTableWidget.setObjectName("fertilizantesTableWidget")
        self.fertilizantesTableWidget.setColumnCount(0)
        self.fertilizantesTableWidget.setRowCount(0)

        self.tabWidget.addTab(self.tabFertilizantes, "Fertilizantes")

    def retranslateUi(self, ProductosControlWindow):
        _translate = QtCore.QCoreApplication.translate
        ProductosControlWindow.setWindowTitle(_translate("ProductosControlWindow", "Gestión de Productos de Control"))
        self.agregarControlPlagasButton.setText(_translate("ProductosControlWindow", "Agregar Control de Plagas"))
        self.editarControlPlagasButton.setText(_translate("ProductosControlWindow", "Editar Control de Plagas"))
        self.eliminarControlPlagasButton.setText(_translate("ProductosControlWindow", "Eliminar Control de Plagas"))
        self.agregarFertilizanteButton.setText(_translate("ProductosControlWindow", "Agregar Fertilizante"))
        self.editarFertilizanteButton.setText(_translate("ProductosControlWindow", "Editar Fertilizante"))
        self.eliminarFertilizanteButton.setText(_translate("ProductosControlWindow", "Eliminar Fertilizante"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ProductosControlWindow = QtWidgets.QMainWindow()
    ui = Ui_ProductosControlWindow()
    ui.setupUi(ProductosControlWindow)
    ProductosControlWindow.show()
    sys.exit(app.exec_())
