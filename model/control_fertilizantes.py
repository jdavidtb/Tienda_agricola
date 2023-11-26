from sqlalchemy import Column, String, Date, ForeignKey
from .producto_control import ProductoControl, Base

class ControlDeFertilizantes(ProductoControl):
    __tablename__ = 'control_de_fertilizantes'

    id = Column(None, ForeignKey('productos_control.id'), primary_key=True)
    fecha_ultima_aplicacion = Column(Date)


    def __init__(self, registro_ica, frecuencia_aplicacion, nombre_producto, valor, fecha_ultima_aplicacion):
        super().__init__(registro_ica, frecuencia_aplicacion, nombre_producto, valor)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion

    def __repr__(self):
        return f"<ControlDeFertilizantes(nombre={self.nombre}, valor={self.valor}, fecha_ultima_aplicacion={self.fecha_ultima_aplicacion})>"
