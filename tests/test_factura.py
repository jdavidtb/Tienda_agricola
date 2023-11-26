# test_factura_controller.py
import unittest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from model.base import Base
from model.factura import Factura
from model.cliente import Cliente  # Asegúrate de que esta importación sea correcta
from model.producto_control import ProductoControl
from model.antibiotico import Antibiotico
from controladores.factura_controller import FacturaController

class TestFacturaController(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = scoped_session(sessionmaker(bind=cls.engine))

    def setUp(self):
        self.session = self.Session()
        try:
            self.trans = self.session.begin_nested()

            # Crear cliente de forma segura
            cliente_existente = self.session.query(Cliente).filter_by(cedula='123456789').first()
            if not cliente_existente:
                self.cliente = Cliente(nombre='Cliente Test', cedula='123456789')
                self.session.add(self.cliente)
                self.session.commit()
            else:
                self.cliente = cliente_existente

            self.controller = FacturaController()
            self.controller.db_service.session = self.session
        except Exception as e:
            self.session.rollback()
            raise e

    def test_crear_factura(self):
        factura = self.controller.crear_factura(cliente_id=self.cliente.id)
        self.assertIsNotNone(factura)
        self.assertEqual(factura.cliente_id, self.cliente.id)

    def test_agregar_producto_a_factura(self):
        factura = self.controller.crear_factura(cliente_id=self.cliente.id)
        producto = ProductoControl(nombre='Producto Test', registro_ica='ICA123', frecuencia_aplicacion='Mensual', valor=100.0)
        self.session.add(producto)
        self.session.commit()

        self.controller.agregar_producto_a_factura(factura.id, producto.id)
        self.assertEqual(len(factura.productos_control), 1)

    def test_eliminar_factura(self):
        factura = self.controller.crear_factura(cliente_id=self.cliente.id)
        self.session.commit()

        self.controller.eliminar_factura(factura.id)
        factura_eliminada = self.controller.obtener_factura_por_id(factura.id)
        self.assertIsNone(factura_eliminada)

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(cls.engine)

if __name__ == '__main__':
    unittest.main()
