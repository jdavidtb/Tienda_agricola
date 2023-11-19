from model.cliente import Cliente
from database.db_service import DBService

class ClienteController:
    def __init__(self):
        self.db_service = DBService()

    def crear_cliente(self, nombre, cedula):
        nuevo_cliente = Cliente(nombre=nombre, cedula=cedula)
        self.db_service.add(nuevo_cliente)

    def obtener_cliente_por_cedula(self, cedula):
        return self.db_service.session.query(Cliente).filter_by(cedula=cedula).first()

    def obtener_todos_los_clientes(self):
        return self.db_service.session.query(Cliente).all()

    def actualizar_cliente(self, cliente_id, nombre=None, cedula=None):
        cliente = self.db_service.session.query(Cliente).get(cliente_id)
        if cliente:
            if nombre:
                cliente.nombre = nombre
            if cedula:
                cliente.cedula = cedula
            self.db_service.session.commit()

    def eliminar_cliente(self, cliente_id):
        cliente = self.db_service.session.query(Cliente).get(cliente_id)
        if cliente:
            self.db_service.session.delete(cliente)
            self.db_service.session.commit()
