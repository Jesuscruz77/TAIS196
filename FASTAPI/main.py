from fastapi import FastAPI
from DB.conexion import  engine, Base 
from routers.usuarios import routerUsuario # sirve para importar la clase APIRouter
from routers.auth import routerAuth # sirve para importar la clase APIRouter


app = FastAPI(
    title="Mi primer API 196",
    description="Jesús Cruz",
    version="1.0.1"
) 

Base.metadata.create_all(bind=engine) # se levanta la tablas definidas en los modelos

app.include_router(routerUsuario) # se incluye el router de usuarios
app.include_router(routerAuth) # se incluye el router de autenticacion


@app.get("/",  tags=["Inicio"]) 
def main(): #
    return {"Hello FastAPI": "Jesús Cruz"}


    
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

# usuarios = [
#     {"id": 1, "nombre": "Jesús Cruz", "correo": "jesus@gmail.com","edad": 21},
#     {"id": 2, "nombre": "Estrella Cuellar", "correo": "estrella@gmail.com", "edad": 20},
#     {"id": 3, "nombre": "Lucero Cuellar", "correo": "lucero@gmail.com", "edad": 20},
#     {"id": 4, "nombre": "Domingo Araujo","correo": "Domi@gmail.com", "edad": 20}
# ]