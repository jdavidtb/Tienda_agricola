from model.antibiotico import Antibiotico
from database.db_service import DBService

class AntibioticoController:
    def __init__(self):
        self.db_service = DBService()

    def crear_antibiotico(self, nombre, dosis, tipo_animal, precio):
        antibiotico = Antibiotico(nombre=nombre, dosis=dosis, tipo_animal=tipo_animal, precio=precio)
        self.db_service.add(antibiotico)
        return antibiotico

    def obtener_antibiotico_por_id(self, antibiotico_id):
        return self.db_service.session.query(Antibiotico).get(antibiotico_id)

    def actualizar_antibiotico(self, antibiotico_id, **datos_actualizados):
        antibiotico = self.obtener_antibiotico_por_id(antibiotico_id)
        if antibiotico:
            for clave, valor in datos_actualizados.items():
                if hasattr(antibiotico, clave):
                    setattr(antibiotico, clave, valor)
            self.db_service.commit()
        else:
            raise ValueError("Antibiótico no encontrado")

    def eliminar_antibiotico(self, antibiotico_id):
        antibiotico = self.obtener_antibiotico_por_id(antibiotico_id)
        if antibiotico:
            self.db_service.delete(antibiotico)
        else:
            raise ValueError("Antibiótico no encontrado")

    def es_producto_antibiotico(self, producto_id):
        antibiotico = self.db_service.session.query(Antibiotico).get(producto_id)
        return antibiotico is not None