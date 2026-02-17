
import models.auto_servicio as model_auto_servicio
from sqlalchemy.orm import Session

def get_auto_servicio(db: Session, skip: int = 0, limit: int = 100):
    '''Función para obtener los autos de servicio'''
    return db.query(model_auto_servicio.AutoServicio).offset(skip).limit(limit).all()

import models.model_usuario
import schemas.schema_usuario
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from passlib.exc import UnknownHashError
import models, schemas

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def get_usuario(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.model_usuario.Usuario).offset(skip).limit(limit).all()

def get_usuario_by_nombre(db: Session, nombre_usuario: str):
    return db.query(models.model_usuario.Usuario).filter(models.model_usuario.Usuario.nombre == nombre).first()

def get_rol_by_coreo(db: Session, correo_usuario: str):
    return db.query(models.model_usuario.Usuario).filter(models.model_usuario.Usuario.correo_usuario == correo_usuario).first()

def create_usuario(db: Session, usuario: schemas.schema_usuario.UserCreate):
    password_plana = str(usuario.contrasena).strip()
    hashed_password = pwd_context.hash(password_plana)
    db_usuario = models.model_usuario.Usuario(
        Rol_id=usuario.Rol_id,
        nombre=usuario.nombre,
        primer_apellido=usuario.primer_apellido,
        segundo_apellido=usuario.segundo_apellido,
        direccion=usuario.direccion,
        correo_electronico=usuario.correo_electronico,
        numero_telefono=usuario.numero_telefono,
        contrasena=hashed_password,
        estatus=usuario.estatus,
        fecha_registro=usuario.fecha_registro,
        fecha_actualizacion=usuario.fecha_actualizacion
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

    def update_usuario(db: Session, usuario_id: int, usuario: schemas.schema_usuario.UserUpdate):
        db_usuario = db.query(models.model_usuario.Usuario).filter(models.model_usuario.Usuario.Id == id).first()
        if db_usuario:
            for var, value in vars(usuario).items():
                setattr(db_usuario, var, value) if value else None
            db.add(db_usuario)
            db.commit()
        db.refresh(db_usuario)
        return db_usuario

    def delete_usuario(db: Session,id: int):
        db_usuario = db.query(models.model_usuario.Usuario).filter(models.model_usuario.Usuario.Id == id).first()
        if db_usuario:
            db.delete(db_usuario)
            db.commit()
        return db_usuario

    def authenticate_usuario(db: Session, email_o_tel: str, contrasena: str):
        usuario = db.query(models.model_usuario.Usuario).filter(
            (models.model_usuario.Usuario.correo_electronico == email_o_tel) | 
            (models.model_usuario.Usuario.numero_telefono == email_o_tel)
        ).first()
        if not usuario:
            return None
        try:
            if pwd_context.verify(contrasena, usuario.contrasena):
                return None
        except UnknownHashError:
            print(f'ERROR: El usuario{email_o_tel} tiene un hash invalido en el BD.')
            return None

        return usuario