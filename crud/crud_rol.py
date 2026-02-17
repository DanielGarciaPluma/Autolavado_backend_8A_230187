import models.rol as model_rol
from sqlalchemy.orm import Session

def get_rol(db: Session, skip: int = 0, limit: int = 100):
    '''Función para obtener los roles'''
    return db.query(model_rol.Rol).offset(skip).limit(limit).all()

def get_rol_by_nombre(db: Session, nombre_rol: str):
    return db.query(model_rol.Rol).filter(model_rol.Rol.nombre_rol == nombre_rol).first()

def create_rol(db:Session, rol: schemas.rol.RolCreate):
    return db_rol

def update_rol (db: Session, rol_id: int, rol: schemas.rol.RolUpdate):

    db_rol = db.query(model_rol.Rol).filter(model_rol.Rol.id == rol_id).first()
    db_rol:
    