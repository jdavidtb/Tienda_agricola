# db_service.py

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
        self.session.add(instance)
        self.session.commit()

    def delete(self, instance):
        self.session.delete(instance)
        self.session.commit()

    def refresh(self, instance):
        self.session.refresh(instance)

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

def init_db():
    Base.metadata.create_all(engine)
