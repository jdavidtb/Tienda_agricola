from model.control_de_plagas import ControlDePlagas
from database.db_service import DBService

class ControlDePlagasController:
    def __init__(self):
        self.db_service = DBService()

    def crear_control_plagas(self, nombre, registro_ica, frecuencia_aplicacion, valor, periodo_carencia):
        control_plagas = ControlDePlagas(nombre=nombre, registro_ica=registro_ica, frecuencia_aplicacion=frecuencia_aplicacion, valor=valor, periodo_carencia=periodo_carencia)
        self.db_service.add(control_plagas)
        return control_plagas

    def obtener_control_plagas_por_id(self, control_plagas_id):
        return self.db_service.session.query(ControlDePlagas).get(control_plagas_id)

    def actualizar_control_plagas(self, control_plagas_id, **datos_actualizados):
        control_plagas = self.obtener_control_plagas_por_id(control_plagas_id)
        if control_plagas:
            for clave, valor in datos_actualizados.items():
                if hasattr(control_plagas, clave):
                    setattr(control_plagas, clave, valor)
            self.db_service.commit()
        else:
            raise ValueError("Control de plagas no encontrado")

    def eliminar_control_plagas(self, control_plagas_id):
        control_plagas = self.obtener_control_plagas_por_id(control_plagas_id)
        if control_plagas:
            self.db_service.delete(control_plagas)
        else:
            raise ValueError("Control de plagas no encontrado")
