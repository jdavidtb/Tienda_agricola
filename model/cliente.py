from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from base import Base


class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    cedula = Column(String, unique=True)
    facturas = relationship('Factura', back_populates='cliente')

    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

