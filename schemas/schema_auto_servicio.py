'''
Docstring for schemas.schema_rol
'''

from pydantic import BaseModel
from datetime import datetime


class Auto_ServicioBase(BaseModel):
    '''Esquema base para los autos de servicio'''
    auto_id:int
    cajero_id:int
    operador_id:int
    servicio_id:int
    fecha:datetime
    status:str
    estado:bool = True
    fecha_registro:datetime
    fecha_actualizacion:datetime

class Auto_ServicioCreate(Auto_ServicioBase):
    '''Esquema para crear un nuevo auto de servicio'''
    pass
class Auto_ServicioUpdate(Auto_ServicioBase):
    '''Esquema para actualizar un auto existente'''
    pass
class Auto_Servicio(Auto_ServicioBase):
    '''Esquema para representar un auto de servicio en la base de datos'''
    id: int

    class Config:
        orm_mode = True