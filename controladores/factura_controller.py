from model.factura import Factura
from model.producto_control import ProductoControl
from model.antibiotico import Antibiotico
from database.db_service import DBService

class FacturaController:
    def __init__(self):
        self.db_service = DBService()

    def crear_factura(self, cliente_id):
        nueva_factura = Factura(cliente_id=cliente_id)
        self.db_service.add(nueva_factura)
        return nueva_factura

    def agregar_producto_a_factura(self, factura_id, producto_id, es_antibiotico=False):
        factura = self.db_service.session.query(Factura).get(factura_id)
        if factura:
            if es_antibiotico:
                producto = self.db_service.session.query(Antibiotico).get(producto_id)
            else:
                producto = self.db_service.session.query(ProductoControl).get(producto_id)

            if producto:
                if es_antibiotico:
                    factura.agregar_antibiotico(producto)
                else:
                    factura.agregar_producto_control(producto)
                self.db_service.commit()
            else:
                raise ValueError("Producto no encontrado")
        else:
            raise ValueError("Factura no encontrada")

    def obtener_factura_por_id(self, factura_id):
        return self.db_service.session.query(Factura).get(factura_id)

    def eliminar_factura(self, factura_id):
        factura = self.obtener_factura_por_id(factura_id)
        if factura:
            self.db_service.delete(factura)


    def actualizar_factura(self, factura_id, cliente_id, productos):
        factura = self.db_service.session.query(Factura).get(factura_id)
        if factura:
            factura.cliente_id = cliente_id
            # Limpiar los productos actuales y agregar los nuevos
            factura.productos_control.clear()
            factura.antibioticos.clear()
            for prod in productos:
                if prod['es_antibiotico']:
                    antibiotico = self.db_service.session.query(Antibiotico).get(prod['id'])
                    factura.agregar_antibiotico(antibiotico)
                else:
                    producto_control = self.db_service.session.query(ProductoControl).get(prod['id'])
                    factura.agregar_producto_control(producto_control)
            self.db_service.commit()
        else:
            raise ValueError("Factura no encontrada")
