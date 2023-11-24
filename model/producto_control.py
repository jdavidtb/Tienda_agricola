from sqlalchemy import Column, Integer, String, Float, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

# Tabla asociativa para la relación muchos a muchos entre Factura y ProductoControl
productos_factura_association = Table('productos_factura', Base.metadata,
    Column('factura_id', Integer, ForeignKey('facturas.id')),
    Column('producto_control_id', Integer, ForeignKey('productos_control.id'))
)

class ProductoControl(Base):
    __tablename__ = 'productos_control'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    registro_ica = Column(String(100))
    frecuencia_aplicacion = Column(String(100))
    valor = Column(Float, nullable=False)
    # Relación muchos a muchos con Factura
    facturas = relationship("Factura", secondary=productos_factura_association, back_populates="productos_control")

    def __init__(self, nombre, registro_ica, frecuencia_aplicacion, valor):
        self.nombre = nombre
        self.registro_ica = registro_ica
        self.frecuencia_aplicacion = frecuencia_aplicacion
        self.valor = valor

    def __repr__(self):
        return f"<ProductoControl(nombre='{self.nombre}', registro_ica='{self.registro_ica}', valor={self.valor})>"
