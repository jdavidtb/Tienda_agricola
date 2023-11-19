from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from datetime import datetime


class Factura(Base):
    __tablename__ = 'facturas'

    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    valor_total = Column(Float, nullable=False)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))

    # Relaciones con Cliente y los productos
    cliente = relationship("Cliente", back_populates="facturas")
    productos_control = relationship("ProductoControl", back_populates="facturas")
    antibioticos = relationship("Antibiotico", back_populates="facturas")

    def __init__(self, cliente_id):
        self.cliente_id = cliente_id
        self.valor_total = 0.0  # Se inicializa en 0 y se calculará al añadir productos

    def agregar_producto_control(self, producto):
        self.productos_control.append(producto)
        self.valor_total += producto.valor

    def agregar_antibiotico(self, antibiotico):
        self.antibioticos.append(antibiotico)
        self.valor_total += antibiotico.valor

    def __repr__(self):
        return f"<Factura(id='{self.id}', fecha='{self.fecha}', valor_total='{self.valor_total}')>"
