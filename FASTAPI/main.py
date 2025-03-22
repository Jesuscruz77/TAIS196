from fastapi import FastAPI, HTTPException, Depends  # type: ignore
from fastapi.responses import JSONResponse  # type: ignore
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

#Endpoint de tipo post que se llama autenticar
@app.post("/auth", tags=["Autenticacion"])
def login(autorizado: modelAuth):
    if autorizado.correo == "jesus@example.com" and autorizado.contrasena == "123456789":
        token:str = createToken(autorizado.model_dump())
        return JSONResponse(content= token)
    else: 
        return {"Aviso": "Usuario no autorizado"}
    

#Endpoint para consultar todos los usuarios
@app.get("/usuarios", dependencies = [Depends(BearerJWT())] , response_model = List[modelUsuario], tags=["Operaciones Crud"])
def ConsultarTodos():
    return usuarios

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

#Endpoint para actualizar el usuario
@app.put("/usuarios/{id}", response_model = modelUsuario, tags=["Operaciones Crud"])
def ActualizarUsuario(id: int, usuario_actualizado: modelUsuario):
    for index,usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuario_actualizado.model_dump()
            return usuarios[index] 
        
    raise HTTPException(status_code=404, detail="El id no esta registrado")

#Endpoint para eliminar un usuario
@app.delete("/usuarios/{id}", tags=["Operaciones Crud"])
def EliminarUsuario(id: int):
    for index,usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(index)
            return {"Mensaje": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="El id no esta registrado")

