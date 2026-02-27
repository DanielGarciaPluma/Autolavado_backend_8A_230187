'''Docstring for schemas.schema_usuario_vehiculo_servicio'''
from datetime import datetime, date, time
from pydantic import BaseModel

class UsuarioVehiculoServicioBase(BaseModel):
    vehiculo_Id: int
    cajero_Id: int
    operativo_Id: int
    servicio_Id: int
    fecha: date
    hora: time
    estatus: str
    estado: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime

class UsuarioVehiculoServicioCreate(UsuarioVehiculoServicioBase):
    pass

class UsuarioVehiculoServicioUpdate(UsuarioVehiculoServicioBase):
    pass

class UsuarioVehiculoServicio(UsuarioVehiculoServicioBase):
    Id: int
    class Config:
        from_attributes = True