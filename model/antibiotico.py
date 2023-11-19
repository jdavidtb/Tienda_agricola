# antibioticos.py

from sqlalchemy import Column, Integer, String, Float
from base import Base


class Antibiotico(Base):
    __tablename__ = 'antibioticos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    dosis = Column(Integer)  # Representado en kg
    tipo_animal = Column(String(50))  # Puede ser 'Bovinos', 'Caprinos', 'Porcinos'
    precio = Column(Float, nullable=False)

    def __init__(self, nombre, dosis, tipo_animal, precio):
        self.nombre = nombre
        self.dosis = dosis
        self.tipo_animal = tipo_animal
        self.precio = precio

    @staticmethod
    def validar_dosis(dosis):
        if 400 <= dosis <= 600:
            return dosis
        else:
            raise ValueError("La dosis debe estar entre 400 y 600")

    def __repr__(self):
        return f"<Antibiotico(nombre='{self.nombre}', tipo_animal='{self.tipo_animal}', precio={self.precio})>"
