from sqlalchemy.orm import Session
import models.model_auto_servicio
import schemas.schema_auto_servicio

def get_auto_servicios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.model_auto_servicio.VehiculoServicio).offset(skip).limit(limit).all()

def get_auto_servicio(db: Session, id: int):
    return db.query(models.model_auto_servicio.VehiculoServicio).filter(models.model_auto_servicio.VehiculoServicio.Id == id).first()

def create_auto_servicio(db: Session, auto_servicio: schemas.schema_auto_servicio.UsuarioVehiculoServicioCreate):
    db_auto_servicio = models.model_auto_servicio.VehiculoServicio(**vars(auto_servicio))
    db.add(db_auto_servicio)
    db.commit()
    db.refresh(db_auto_servicio)
    return db_auto_servicio

def update_auto_servicio(db: Session, id: int, auto_servicio: schemas.schema_auto_servicio.UsuarioVehiculoServicioUpdate):
    db_auto_servicio = db.query(models.model_auto_servicio.VehiculoServicio).filter(models.model_auto_servicio.VehiculoServicio.Id == id).first()
    if db_auto_servicio:
        for var, value in vars(auto_servicio).items():
            if value is not None:
                setattr(db_auto_servicio, var, value)
        db.add(db_auto_servicio)
        db.commit()
        db.refresh(db_auto_servicio)
    return db_auto_servicio

def delete_auto_servicio(db: Session, id: int):
    db_auto_servicio = db.query(models.model_auto_servicio.VehiculoServicio).filter(models.model_auto_servicio.VehiculoServicio.Id == id).first()
    if db_auto_servicio:
        db.delete(db_auto_servicio)
        db.commit()
    return db_auto_servicio