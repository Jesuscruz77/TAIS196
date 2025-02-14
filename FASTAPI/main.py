from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="Mi primer API 196",
    description="Jesús Cruz",
    version="1.0.1"
) 

usuarios = [
    {"id": 1, "nombre": "Jesús Cruz", "edad": 21},
    {"id": 2, "nombre": "Estrella Cuellar", "edad": 20},
    {"id": 3, "nombre": "Lucero Cuellar", "edad": 20},
    {"id": 4, "nombre": "Domingo Araujo", "edad": 20}
]

@app.get("/",  tags=["Inicio"]) 
def main(): #
    return {"Hello FastAPI": "Jesús Cruz"}

#Endpoint para consultar todos los usuarios
@app.get("/usuarios", tags=["Operaciones Crud"])
def ConsultarTodos():
    return {"Usuarios Registrados": usuarios}

#Endpoint para agregar un usuario
@app.post("/usuarios/", tags=["Operaciones Crud"])
def AgregarUsuario(usuario: dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="El id ya esta registrado")
        
    usuarios.append(usuario)
    return usuario

#Endpoint para actualizar el usuario
@app.put("/usuarios/{id}", tags=["Operaciones Crud"])
def ActualizarUsuario(id: int, usuario: dict):
    for index,usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuario)
            return usuarios[index, "Mensaje": "Usuario actualizado"] 
    raise HTTPException(status_code=404, detail="El id no esta registrado")

#Endpoint para eliminar un usuario
@app.delete("/usuarios/{id}", tags=["Operaciones Crud"])
def EliminarUsuario(id: int):
    for index,usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(index)
            return {"Mensaje": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="El id no esta registrado")