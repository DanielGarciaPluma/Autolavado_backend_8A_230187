'''Docstring for schemas.schema_servicio'''
from datetime import datetime
from pydantic import BaseModel

class ServicioBase(BaseModel):
    nombre: str
    descripcion: str
    costo: float
    duracion_minutos: int
    estado: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime

class ServicioCreate(ServicioBase):
    pass

class ServicioUpdate(ServicioBase):
    pass

class Servicio(ServicioBase):
    Id: int
    class Config:
        from_attributes = True