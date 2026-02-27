from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import config.db
import crud.crud_services
import schemas.schema_servicio
import models.model_services
import auth

servicio = APIRouter()
models.model_services.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@servicio.get("/servicio/", response_model=List[schemas.schema_servicio.Servicio], tags=["Servicios"])
async def read_servicios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    return crud.crud_services.get_servicios(db=db, skip=skip, limit=limit)

@servicio.post("/servicio/", response_model=schemas.schema_servicio.Servicio, tags=["Servicios"])
def create_servicio(servicio_data: schemas.schema_servicio.ServicioCreate, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    return crud.crud_services.create_servicio(db=db, servicio=servicio_data)

@servicio.put("/servicio/{id}", response_model=schemas.schema_servicio.Servicio, tags=["Servicios"])
async def update_servicio(id: int, servicio_data: schemas.schema_servicio.ServicioUpdate, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    db_servicio = crud.crud_services.update_servicio(db=db, id=id, servicio=servicio_data)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no existe")
    return db_servicio

@servicio.delete("/servicio/{id}", response_model=schemas.schema_servicio.Servicio, tags=["Servicios"])
async def delete_servicio(id: int, db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    db_servicio = crud.crud_services.delete_servicio(db=db, id=id)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no existe")
    return db_servicio