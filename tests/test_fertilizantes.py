import unittest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from model.base import Base
from model.control_fertilizantes import ControlDeFertilizantes
from controladores.control_fertilizantesController import ControlDeFertilizantesController

class TestControlDeFertilizantesController(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = scoped_session(sessionmaker(bind=cls.engine))

    def setUp(self):
        self.session = self.Session()
        self.trans = self.session.begin_nested()
        self.controller = ControlDeFertilizantesController()
        self.controller.db_service.session = self.session

    def test_crear_fertilizante(self):
        fecha = datetime.now().date()
        fertilizante = self.controller.crear_fertilizante('Nitrofoska', 'ICA12345', 'Mensual', 150.0, fecha)
        self.assertIsNotNone(fertilizante)
        self.assertEqual(fertilizante.nombre, 'Nitrofoska')

    def test_obtener_fertilizante_por_id(self):
        fecha = datetime.now().date()
        # Asegúrate de que los argumentos estén en el orden correcto: primero el nombre, luego el registro_ica
        fertilizante = ControlDeFertilizantes('Superfosfato', 'ICA54321', 'Bimensual', 200.0, fecha)
        self.session.add(fertilizante)
        self.session.commit()

        fertilizante_obtenido = self.controller.obtener_fertilizante_por_id(fertilizante.id)
        self.assertEqual(fertilizante_obtenido.nombre, 'Superfosfato')  # Verificando el nombre correcto

    def test_actualizar_fertilizante(self):
        fecha = datetime.now().date()
        fertilizante = ControlDeFertilizantes('ICA98765', 'Trimestral', 'Urea', 120.0, fecha)
        self.session.add(fertilizante)
        self.session.commit()

        self.controller.actualizar_fertilizante(fertilizante.id, nombre='Urea Plus')  # Cambio aquí
        fertilizante_actualizado = self.controller.obtener_fertilizante_por_id(fertilizante.id)
        self.assertEqual(fertilizante_actualizado.nombre, 'Urea Plus')  # Cambio aquí

    def test_eliminar_fertilizante(self):
        fecha = datetime.now().date()
        fertilizante = ControlDeFertilizantes('ICA11111', 'Anual', 'Potasa', 180.0, fecha)
        self.session.add(fertilizante)
        self.session.commit()

        self.controller.eliminar_fertilizante(fertilizante.id)
        fertilizante_eliminado = self.controller.obtener_fertilizante_por_id(fertilizante.id)
        self.assertIsNone(fertilizante_eliminado)

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(cls.engine)

if __name__ == '__main__':
    unittest.main()
