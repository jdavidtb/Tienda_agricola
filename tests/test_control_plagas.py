
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from model.base import Base
from model.control_de_plagas import ControlDePlagas
from controladores.control_plagasController import ControlDePlagasController

class TestControlDePlagasController(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = scoped_session(sessionmaker(bind=cls.engine))

    def setUp(self):
        self.session = self.Session()
        self.trans = self.session.begin_nested()
        self.controller = ControlDePlagasController()
        self.controller.db_service.session = self.session

    def test_crear_control_plagas(self):
        control_plagas = self.controller.crear_control_plagas('Nombre', 'RegistroICA', 'Frecuencia', 100.0, 'PeriodoCarencia')
        self.assertIsNotNone(control_plagas)
        self.assertEqual(control_plagas.nombre_producto, 'Nombre')

    def test_obtener_control_plagas_por_id(self):
        control_plagas = ControlDePlagas('RegistroICA', 'Frecuencia', 'Nombre', 100.0, 'PeriodoCarencia')
        self.session.add(control_plagas)
        self.session.commit()

        control_plagas_obtenido = self.controller.obtener_control_plagas_por_id(control_plagas.id)
        self.assertEqual(control_plagas_obtenido.nombre_producto, 'Nombre')

    def test_actualizar_control_plagas(self):
        control_plagas = ControlDePlagas('RegistroICA', 'Frecuencia', 'Nombre', 100.0, 'PeriodoCarencia')
        self.session.add(control_plagas)
        self.session.commit()

        self.controller.actualizar_control_plagas(control_plagas.id, nombre_producto='Nombre Actualizado')
        control_plagas_actualizado = self.controller.obtener_control_plagas_por_id(control_plagas.id)
        self.assertEqual(control_plagas_actualizado.nombre_producto, 'Nombre Actualizado')

    def test_eliminar_control_plagas(self):
        control_plagas = ControlDePlagas('RegistroICA', 'Frecuencia', 'Nombre', 100.0, 'PeriodoCarencia')
        self.session.add(control_plagas)
        self.session.commit()

        self.controller.eliminar_control_plagas(control_plagas.id)
        control_plagas_eliminado = self.controller.obtener_control_plagas_por_id(control_plagas.id)
        self.assertIsNone(control_plagas_eliminado)

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(cls.engine)

if __name__ == '__main__':
    unittest.main()
