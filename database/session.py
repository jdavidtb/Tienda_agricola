from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.base import Base

DATABASE_URL = "sqlite:///tienda_agricola.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)