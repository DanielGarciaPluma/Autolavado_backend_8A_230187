''' En esta clase permite generar el model para los tipos de rol'''
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base

class Rol(Base):
    '''Clase para especificar la tabla roles de usuario'''
    _tablemname_="tbc_roles"

    Id = Column(Integer, primary_key=True, index=True)
    nombreRol = Column(String(15))
    estado = Column(Boolean)
    