from fastapi import FastAPI, HTTPException, Depends  # type: ignore
from fastapi.responses import JSONResponse  # type: ignore
from fastapi.encoders import jsonable_encoder  # type: ignore Sirve para convertir un objeto en un diccionario
from typing import Optional, List
from modelsPydantic import modelUsuario, modelAuth
from tokenGen import createToken
from middlewares import BearerJWT
from DB.conexion import Session, engine, Base 
from models.modelsDB import User # sirve para importar la clase User y la clase Base


app = FastAPI(
    title="Mi primer API 196",
    description="Jesús Cruz",
    version="1.0.1"
) 

Base.metadata.create_all(bind=engine) # se levanta la tablas definidas en los modelos

usuarios = [
    {"id": 1, "nombre": "Jesús Cruz", "correo": "jesus@gmail.com","edad": 21},
    {"id": 2, "nombre": "Estrella Cuellar", "correo": "estrella@gmail.com", "edad": 20},
    {"id": 3, "nombre": "Lucero Cuellar", "correo": "lucero@gmail.com", "edad": 20},
    {"id": 4, "nombre": "Domingo Araujo","correo": "Domi@gmail.com", "edad": 20}
]

@app.get("/",  tags=["Inicio"]) 
def main(): #
    return {"Hello FastAPI": "Jesús Cruz"}



#Endpoint para consultar todos los usuarios
@app.get("/usuarios", tags=["Operaciones Crud"])
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
@app.get("/usuarios/{id}", tags=["Operaciones Crud"])
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
@app.post("/usuarios/", response_model = modelUsuario, tags=["Operaciones Crud"])
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
@app.put("/usuarios/{id}", response_model = modelUsuario, tags=["Operaciones Crud"])
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
@app.delete("/usuarios/{id}", tags=["Operaciones Crud"])
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




# #Endpoint para actualizar el usuario
# @app.put("/usuarios/{id}", response_model = modelUsuario, tags=["Operaciones Crud"])
# def ActualizarUsuario(id: int, usr_act: modelUsuario):
#     for index,usr in enumerate(usuarios):
#         if usr["id"] == id:
#             usuarios[index] = usr_act.model_dump()
#             return usuarios[index] 
        
#     raise HTTPException(status_code=404, detail="El id no esta registrado")

# #Endpoint para eliminar un usuario
# @app.delete("/usuarios/{id}", tags=["Operaciones Crud"])
# def EliminarUsuario(id: int):
#     for index,usr in enumerate(usuarios):
#         if usr["id"] == id:
#             usuarios.pop(index)
#             return {"Mensaje": "Usuario eliminado"}
#     raise HTTPException(status_code=404, detail="El id no esta registrado")

#Endpoint de tipo post que se llama autenticar
@app.post("/auth", tags=["Autenticacion"])
def login(autorizado: modelAuth):
    if autorizado.correo == "jesus@example.com" and autorizado.contrasena == "123456789":
        token:str = createToken(autorizado.model_dump())
        return JSONResponse(content= token)
    else: 
        return {"Aviso": "Usuario no autorizado"}
    