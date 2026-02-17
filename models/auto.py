'''Este archivo define el modelo de auto en la base de datos'''
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey,DateTime
from config.db import Base

class Auto(Base):
    '''Modelo para la tabla de autos'''
    __tablename__ = "tbb_autos"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer,ForeignKey("tbc_usuarios.id"))
    modelo = Column(String(50), nullable=False)
    placa = Column(String(20), unique=True, index=True, nullable=False)
    serie = Column(String(50), nullable=False)
    color = Column(String(30), nullable=False)
    tipo = Column(String(30), nullable=False)
    anio =Column (Integer, nullable=False)
    estado =Column(Boolean, default=True)
    fecha_registro= Column(DateTime)
    fecha_actualizacion= Column(DateTime)
    marca= Column(String(50), nullable=False)
