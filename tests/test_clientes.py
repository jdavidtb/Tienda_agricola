import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.cliente import Cliente, Base
from controladores.clientes_controller import ClienteController

class TestClienteController(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configura una base de datos de prueba (podría ser SQLite en memoria)
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)  # Crear las tablas en la base de datos de prueba
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

    def setUp(self):
        # Inicializa aquí el controlador y cualquier otro setup antes de cada prueba
        self.controller = ClienteController()
        self.controller.db_service.session = self.session  # Asegúrate de que el controlador use la sesión de prueba

    def test_crear_cliente(self):
        self.controller.crear_cliente('Juan Perez', '12345678')
        cliente_creado = self.session.query(Cliente).filter_by(cedula='12345678').first()
        self.assertIsNotNone(cliente_creado)
        self.assertEqual(cliente_creado.nombre, 'Juan Perez')

    def test_obtener_cliente_por_cedula(self):
        # Asegúrate de que hay un cliente en la base de datos de prueba para buscar
        cliente = Cliente(nombre='Ana Gomez', cedula='87654321')
        self.session.add(cliente)
        self.session.commit()

        cliente_encontrado = self.controller.obtener_cliente_por_cedula('87654321')
        self.assertIsNotNone(cliente_encontrado)
        self.assertEqual(cliente_encontrado.nombre, 'Ana Gomez')

    # Continúa escribiendo pruebas para actualizar_cliente, eliminar_cliente, etc.

    @classmethod
    def tearDownClass(cls):
        # Cierra la conexión y destruye la base de datos de prueba
        cls.session.close()
        Base.metadata.drop_all(cls.engine)

if __name__ == '__main__':
    unittest.main()
