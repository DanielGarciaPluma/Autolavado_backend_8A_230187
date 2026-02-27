from sqlalchemy.orm import Session
import models.model_auto 
import schemas.schema_auto

def get_vehiculos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.model_auto.Vehiculo).offset(skip).limit(limit).all()

def get_vehiculo(db: Session, id: int):
    return db.query(models.model_auto.Vehiculo).filter(models.model_auto.Vehiculo.Id == id).first()

def create_vehiculo(db: Session, vehiculo: schemas.schema_auto.VehiculoCreate):
    # Desempaquetamos los datos del esquema directamente al modelo
    db_vehiculo = models.model_auto.Vehiculo(**vars(vehiculo))
    db.add(db_vehiculo)
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

def update_vehiculo(db: Session, id: int, vehiculo: schemas.schema_auto.VehiculoUpdate):
    db_vehiculo = db.query(models.model_auto.Vehiculo).filter(models.model_auto.Vehiculo.Id == id).first()
    
    if db_vehiculo:
        for var, value in vars(vehiculo).items():
            # Actualizamos solo si el valor no es nulo (para no borrar datos accidentalmente)
            if value is not None:
                setattr(db_vehiculo, var, value)
        db.add(db_vehiculo)
        db.commit()
        db.refresh(db_vehiculo)
        
    return db_vehiculo

def delete_vehiculo(db: Session, id: int):
    db_vehiculo = db.query(models.model_auto.Vehiculo).filter(models.model_auto.Vehiculo.Id == id).first()
    if db_vehiculo:
        db.delete(db_vehiculo)
        db.commit()
    return db_vehiculo