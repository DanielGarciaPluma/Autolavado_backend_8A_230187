from sqlalchemy.orm import Session
import models.model_services
import schemas.schema_servicio

def get_servicios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.model_services.Servicios).offset(skip).limit(limit).all()

def get_servicio(db: Session, id: int):
    return db.query(models.model_services.Servicios).filter(models.model_services.Servicios.Id == id).first()

def create_servicio(db: Session, servicio: schemas.schema_servicio.ServicioCreate):
    db_servicio = models.model_services.Servicios(**vars(servicio))
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

def update_servicio(db: Session, id: int, servicio: schemas.schema_servicio.ServicioUpdate):
    db_servicio = db.query(models.model_services.Servicios).filter(models.model_services.Servicios.Id == id).first()
    if db_servicio:
        for var, value in vars(servicio).items():
            if value is not None:
                setattr(db_servicio, var, value)
        db.add(db_servicio)
        db.commit()
        db.refresh(db_servicio)
    return db_servicio

def delete_servicio(db: Session, id: int):
    db_servicio = db.query(models.model_services.Servicios).filter(models.model_services.Servicios.Id == id).first()
    if db_servicio:
        db.delete(db_servicio)
        db.commit()
    return db_servicio