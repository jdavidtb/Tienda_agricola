# test_producto_control.py
import unittest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from model.base import Base
from model.producto_control import ProductoControl
from controladores.producto_controlController import ProductoControlController

class TestProductoControlController(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = scoped_session(sessionmaker(bind=cls.engine))

    def setUp(self):
        self.session = self.Session()
        self.trans = self.session.begin_nested()
        self.controller = ProductoControlController()
        self.controller.db_service.session = self.session


    def test_obtener_producto_por_id(self):
        producto = ProductoControl(nombre='Producto Test', registro_ica='ICA123', frecuencia_aplicacion='Mensual', valor=100.0)
        self.session.add(producto)
        self.session.commit()

        producto_obtenido = self.controller.obtener_producto_por_id(producto.id)
        self.assertEqual(producto_obtenido.nombre, 'Producto Test')

    def test_actualizar_producto_control(self):
        producto = ProductoControl(nombre='Producto Test', registro_ica='ICA123', frecuencia_aplicacion='Mensual', valor=100.0)
        self.session.add(producto)
        self.session.commit()

        self.controller.actualizar_producto_control(producto.id, nombre='Producto Actualizado')
        producto_actualizado = self.controller.obtener_producto_por_id(producto.id)
        self.assertEqual(producto_actualizado.nombre, 'Producto Actualizado')

    def test_eliminar_producto_control(self):
        producto = ProductoControl(nombre='Producto Test', registro_ica='ICA123', frecuencia_aplicacion='Mensual', valor=100.0)
        self.session.add(producto)
        self.session.commit()

        self.controller.eliminar_producto_control(producto.id)
        producto_eliminado = self.controller.obtener_producto_por_id(producto.id)
        self.assertIsNone(producto_eliminado)

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(cls.engine)

if __name__ == '__main__':
    unittest.main()
