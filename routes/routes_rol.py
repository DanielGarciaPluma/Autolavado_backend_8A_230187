from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud.crud_rol as crud_rol
import config.db as db_config
import schemas.schema_rol as schema_rol
import models.rol as model_rol

@rol.get("/rol", response_model=list[schema_rol.Rol], tags=["Roles"])
def get_rol(skip: int = 0, limit: int = 100, db: Session = Depends(db_config.get_db)):
    return db_rol

@rol.post("rol", response_model=schema_rol.Rol,tags=["Roles"])
def create_rol(rol: schema_rol.RolCreate, db: Session = Depends(db_config.get_db)):
    db_rol = crud_rol.get_rol_by_nombre(db, nombre_rol=rol.nombre_rol)
    if db_rol:
        raise HTTPException(status_code=400, detail="El rol ya existe, intenta nuevamente")
    return crud.crud_rol.create_rol(db=db, rol=rol)

@rol.put("/rol/(id)", response_model=schemas.schema_rol.Rol, tags=["Roles"])
async def update_rol(id: int, rol: schema_rol.RolUpdate, db: Session = Depends(get_db)):
    if db_rol = crud.crud_rol.update_rol(db=db, rol_id=id, rol=rol):
        raise HTTPException(status_code=404, detail="El rol no existe, no actualizado")
    return db_rol

@rol.delete("/rol/(id)", response_model=schemas.schema_rol.Rol, tags=["Roles"])
async def delete_rol(id: int, db: Session = Depends(get_db)):
    db_rol = crud.crud_rol.delete_rol(db=db, rol_id=id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="El rol no existe, no se puede eliminar")
    return db_rol