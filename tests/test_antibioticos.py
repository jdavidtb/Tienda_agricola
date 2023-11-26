import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from model.base import Base
from model.antibiotico import Antibiotico
from controladores.anbioticoController import AntibioticoController

class TestAntibioticoController(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = scoped_session(sessionmaker(bind=cls.engine))

    def setUp(self):
        self.session = self.Session()
        self.trans = self.session.begin_nested()
        self.controller = AntibioticoController()
        self.controller.db_service.session = self.session

    def test_crear_antibiotico(self):
        antibiotico = self.controller.crear_antibiotico('Amoxicilina', 500, 'Bovinos', 20.0)
        self.assertIsNotNone(antibiotico)
        self.assertEqual(antibiotico.nombre, 'Amoxicilina')

    def test_obtener_antibiotico_por_id(self):
        antibiotico = Antibiotico(nombre='Penicilina', dosis=500, tipo_animal='Porcinos', precio=30.0)
        self.session.add(antibiotico)
        self.session.commit()

        antibiotico_obtenido = self.controller.obtener_antibiotico_por_id(antibiotico.id)
        self.assertEqual(antibiotico_obtenido.nombre, 'Penicilina')

    def test_actualizar_antibiotico(self):
        antibiotico = Antibiotico(nombre='Tetraciclina', dosis=500, tipo_animal='Caprinos', precio=25.0)
        self.session.add(antibiotico)
        self.session.commit()

        self.controller.actualizar_antibiotico(antibiotico.id, nombre='Tetraciclina Plus', precio=27.0)
        antibiotico_actualizado = self.controller.obtener_antibiotico_por_id(antibiotico.id)
        self.assertEqual(antibiotico_actualizado.nombre, 'Tetraciclina Plus')
        self.assertEqual(antibiotico_actualizado.precio, 27.0)

    def test_eliminar_antibiotico(self):
        antibiotico = Antibiotico(nombre='Clindamicina', dosis=500, tipo_animal='Bovinos', precio=40.0)
        self.session.add(antibiotico)
        self.session.commit()

        self.controller.eliminar_antibiotico(antibiotico.id)
        antibiotico_eliminado = self.controller.obtener_antibiotico_por_id(antibiotico.id)
        self.assertIsNone(antibiotico_eliminado)

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(cls.engine)

if __name__ == '__main__':
    unittest.main()
