from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud.crud_rol as crud_rol
import config.db as db_config
import schemas.schema_rol as schema_rol
import models.rol as model_rol