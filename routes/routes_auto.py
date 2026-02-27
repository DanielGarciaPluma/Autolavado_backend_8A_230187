from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import config.db
import crud.crud_auto
import schemas.schema_auto
import models.model_auto
import auth

auto = APIRouter()

# Esto crea la tabla si no existe
models.model_auto.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@auto.get("/auto/", response_model=List[schemas.schema_auto.Vehiculo], tags=["Autos"])
async def read_autos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    return crud.crud_auto.get_vehiculos(db=db, skip=skip, limit=limit)

@auto.get("/auto/{id}", response_model=schemas.schema_auto.Vehiculo, tags=["Autos"])
async def read_auto(id: int, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    db_vehiculo = crud.crud_auto.get_vehiculo(db=db, id=id)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return db_vehiculo

@auto.post("/auto/", response_model=schemas.schema_auto.Vehiculo, tags=["Autos"])
def create_auto(vehiculo: schemas.schema_auto.VehiculoCreate, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    return crud.crud_auto.create_vehiculo(db=db, vehiculo=vehiculo)

@auto.put("/auto/{id}", response_model=schemas.schema_auto.Vehiculo, tags=["Autos"])
async def update_auto(id: int, vehiculo: schemas.schema_auto.VehiculoUpdate, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    db_vehiculo = crud.crud_auto.update_vehiculo(db=db, id=id, vehiculo=vehiculo)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="Vehículo no existe, no actualizado")
    return db_vehiculo

@auto.delete("/auto/{id}", response_model=schemas.schema_auto.Vehiculo, tags=["Autos"])
async def delete_auto(id: int, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    db_vehiculo = crud.crud_auto.delete_vehiculo(db=db, id=id)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="El Vehículo no existe, no se pudo eliminar")
    return db_vehiculo