from fastapi import FastAPI, HTTPException, Depends  # type: ignore
from fastapi.responses import JSONResponse  # type: ignore
from fastapi.encoders import jsonable_encoder  # type: ignore Sirve para convertir un objeto en un diccionario
from modelsPydantic import modelUsuario
from middlewares import BearerJWT
from DB.conexion import Session
from models.modelsDB import User # sirve para importar la clase User y la clase Base
from fastapi import APIRouter # sirve para importar la clase APIRouter

routerUsuario = APIRouter() # se crea una instancia de la clase APIRouter

#Depends(BearerJWT()) # se importa el middleware de autenticacion BearerJWT

#Endpoint para consultar todos los usuarios
@routerUsuario.get("/usuarios", tags=["Operaciones Crud"])
def ConsultarTodos():
    db = Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content= jsonable_encoder(consulta))
    except Exception as x:
        return JSONResponse(status_code=500, content={"mensaje": "No fue posible consultar usuarios", "error": str(x)})
    finally:
        db.close()
    
#Endpoint para consultar un usuario por id
@routerUsuario.get("/usuarios/{id}", tags=["Operaciones Crud"])
def ConsultarUno(id: int):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if not consulta:
            raise HTTPException(status_code=404, content = {"mensaje": "Usuario no encontrado"})
        return JSONResponse(content= jsonable_encoder(consulta))
        
    except Exception as x:
        return JSONResponse(status_code=500, content={"mensaje": "No fue posible consultar usuarios", "error": str(x)})
    finally:
        db.close()


#Endpoint para agregar un usuario
@routerUsuario.post("/usuarios/", response_model = modelUsuario, tags=["Operaciones Crud"])
def AgregarUsuario(usuarionuevo: modelUsuario):
    db = Session()
    try:
        db.add(User(**usuarionuevo.model_dump()))
        db.commit()
        return JSONResponse(status_code=201, content={"mensaje": "Usuario creado", "usuario": usuarionuevo.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"mensaje": "Error al crear el usuario", "error": str(e)})
    finally:
        db.close()

#Endpoint para actualizar un usuario
@routerUsuario.put("/usuarios/{id}", response_model = modelUsuario, tags=["Operaciones Crud"])
def ActualizarUsuario(id: int, usr_act: modelUsuario):
    db = Session()
    try:
        actualizar = db.query(User).filter(User.id == id).first()
        if not actualizar:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        for key, value in usr_act.model_dump().items():
            setattr(actualizar, key, value)
        db.commit()
        return JSONResponse(content={"mensaje": "Usuario actualizado", "usuario": usr_act.model_dump()})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"mensaje": "Error al actualizar el usuario", "error": str(e)})
    
    finally:
        db.close()


#Endpoint para eliminar un usuario
@routerUsuario.delete("/usuarios/{id}", tags=["Operaciones Crud"])
def EliminarUsuario(id: int):
    db = Session()
    try:
        eliminar = db.query(User).filter(User.id == id).first()
        if not eliminar:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        db.delete(eliminar)
        db.commit()
        return JSONResponse(content={"mensaje": "Usuario eliminado"})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"mensaje": "Error al eliminar el usuario", "error": str(e)})
    
    finally:
        db.close()