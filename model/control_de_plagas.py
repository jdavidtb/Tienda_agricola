from sqlalchemy import Column, String, Date, ForeignKey
from .producto_control import ProductoControl, Base

class ControlDePlagas(ProductoControl):
    __tablename__ = 'control_de_plagas'

    id = Column(None, ForeignKey('productos_control.id'), primary_key=True)
    periodo_carencia = Column(String)

    def __init__(self, registro_ica, frecuencia_aplicacion, nombre_producto, valor, periodo_carencia):
        super().__init__(registro_ica, frecuencia_aplicacion, nombre_producto, valor)
        self.nombre_producto = nombre_producto
        self.periodo_carencia = periodo_carencia
    def __repr__(self):
        return f"<ControlDePlagas(nombre={self.nombre_producto}, valor={self.valor}, periodo_carencia={self.periodo_carencia})>"
