import models.auto_servicio as model_auto_servicio
from sqlalchemy.orm import Session  

def get_auto_servicio(db: Session, skip: int = 0, limit: int = 100):
    '''Función para obtener los autos de servicio'''
    return db.query(model_auto_servicio.AutoServicio).offset(skip).limit(limit).all()
