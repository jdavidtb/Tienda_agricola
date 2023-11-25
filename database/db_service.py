# db_service.py
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model.base import Base

DATABASE_URL = "sqlite:///tienda_agricola.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class DBService:
    def __init__(self):
        self.session = Session()

    def add(self, instance):
        print(f"Agregando instancia a la base de datos: {instance}")
        try:
            self.session.add(instance)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


    def delete(self, instance):
        self.session.delete(instance)
        self.session.commit()

    def refresh(self, instance):
        self.session.refresh(instance)

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()


    def test_connection(self):
        try:
            self.session.execute(text('SELECT 1'))
            return True
        except Exception as e:
            print(f"Error al conectar con la base de datos: {e}")
            return False


def init_db():
    Base.metadata.create_all(engine)
