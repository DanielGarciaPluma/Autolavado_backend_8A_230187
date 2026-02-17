import models.rol as model_rol
from sqlalchemy.orm import Session

def get_rol(db: Session, skip: int = 0, limit: int = 100):
    '''Función para obtener los roles'''
    return db.query(model_rol.Rol).offset(skip).limit(limit).all()