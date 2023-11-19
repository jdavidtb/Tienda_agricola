from model.control_fertilizantes import ControlDeFertilizantes
from database.db_service import DBService

class ControlDeFertilizantesController:
    def __init__(self):
        self.db_service = DBService()

    def crear_fertilizante(self, nombre, registro_ica, frecuencia_aplicacion, valor, fecha_ultima_aplicacion):
        fertilizante = ControlDeFertilizantes(nombre=nombre, registro_ica=registro_ica, frecuencia_aplicacion=frecuencia_aplicacion, valor=valor, fecha_ultima_aplicacion=fecha_ultima_aplicacion)
        self.db_service.add(fertilizante)
        return fertilizante

    def obtener_fertilizante_por_id(self, fertilizante_id):
        return self.db_service.session.query(ControlDeFertilizantes).get(fertilizante_id)

    def actualizar_fertilizante(self, fertilizante_id, **datos_actualizados):
        fertilizante = self.obtener_fertilizante_por_id(fertilizante_id)
        if fertilizante:
            for clave, valor in datos_actualizados.items():
                if hasattr(fertilizante, clave):
                    setattr(fertilizante, clave, valor)
            self.db_service.commit()
        else:
            raise ValueError("Fertilizante no encontrado")

    def eliminar_fertilizante(self, fertilizante_id):
        fertilizante = self.obtener_fertilizante_por_id(fertilizante_id)
        if fertilizante:
            self.db_service.delete(fertilizante)
        else:
            raise ValueError("Fertilizante no encontrado")
