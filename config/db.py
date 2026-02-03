'''Establce la conexion con el servidor de la base de datos'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql://root:1234@localhost:3307/autolavadodb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionlocal = sessionmaker(aoutocommit =False, aotuflush=False, bind=engine)
Base =declarative_base()

