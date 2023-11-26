from model.producto_control import ProductoControl
from model.control_fertilizantes import ControlDeFertilizantes
from model.control_de_plagas import ControlDePlagas
from database.db_service import DBService


class ProductoControlController:
    def __init__(self):
        self.db_service = DBService()

    def crear_producto_control(self, tipo_producto, **datos_producto):
        if tipo_producto == 'plaga':
            producto = ControlDePlagas(**datos_producto)
        elif tipo_producto == 'fertilizante':
            producto = ControlDeFertilizantes(**datos_producto)
        else:
            raise ValueError("Tipo de producto no reconocido")

        self.db_service.add(producto)
        return producto

    def obtener_producto_por_id(self, producto_id):
        return self.db_service.session.get(ProductoControl, producto_id)

    def actualizar_producto_control(self, producto_id, **datos_actualizados):
        producto = self.obtener_producto_por_id(producto_id)
        if producto:
            for clave, valor in datos_actualizados.items():
                if hasattr(producto, clave):
                    setattr(producto, clave, valor)
            self.db_service.commit()
        else:
            raise ValueError("Producto no encontrado")

    def eliminar_producto_control(self, producto_id):
        producto = self.obtener_producto_por_id(producto_id)
        if producto:
            self.db_service.delete(producto)
        else:
            raise ValueError("Producto no encontrado")

    def obtener_producto_por_nombre(self, nombre_producto):
        return self.db_service.session.query(ProductoControl).filter_by(nombre=nombre_producto).first()