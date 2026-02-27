from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import config.db
import crud.crud_auto_servicio
import schemas.schema_auto_servicio
import models.model_auto_servicio
import auth

auto_servicio = APIRouter()
models.model_auto_servicio.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@auto_servicio.get("/auto-servicio/", response_model=List[schemas.schema_auto_servicio.UsuarioVehiculoServicio], tags=["Ventas y Asignaciones"])
async def read_auto_servicios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    return crud.crud_auto_servicio.get_auto_servicios(db=db, skip=skip, limit=limit)

@auto_servicio.post("/auto-servicio/", response_model=schemas.schema_auto_servicio.UsuarioVehiculoServicio, tags=["Ventas y Asignaciones"])
def create_auto_servicio(data: schemas.schema_auto_servicio.UsuarioVehiculoServicioCreate, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    return crud.crud_auto_servicio.create_auto_servicio(db=db, auto_servicio=data)

@auto_servicio.put("/auto-servicio/{id}", response_model=schemas.schema_auto_servicio.UsuarioVehiculoServicio, tags=["Ventas y Asignaciones"])
async def update_auto_servicio(id: int, data: schemas.schema_auto_servicio.UsuarioVehiculoServicioUpdate, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    db_auto_servicio = crud.crud_auto_servicio.update_auto_servicio(db=db, id=id, auto_servicio=data)
    if db_auto_servicio is None:
        raise HTTPException(status_code=404, detail="Registro no existe")
    return db_auto_servicio

@auto_servicio.delete("/auto-servicio/{id}", response_model=schemas.schema_auto_servicio.UsuarioVehiculoServicio, tags=["Ventas y Asignaciones"])
async def delete_auto_servicio(id: int, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    db_auto_servicio = crud.crud_auto_servicio.delete_auto_servicio(db=db, id=id)
    if db_auto_servicio is None:
        raise HTTPException(status_code=404, detail="Registro no existe")
    return db_auto_servicio