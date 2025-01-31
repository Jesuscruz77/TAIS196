from fastapi import FastAPI
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

@app.get("/promedio", tags=["Promedio"])
def promedio():
    return {"Promedio": 8.5}

#Parametro obligatorio
@app.get("/usuario/{id}", tags=["Parametro obligatorio"])
def consultausuario(id: int):
    #conectamos a una BD
    #Hacemos consulta retornamos resultset
    return {"Se encontro el usuario": id}

#Parametro opcional
@app.get("/usuario2/", tags=["Parametro opcional"])
def consultausuario2(id: Optional[int] = None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id:
                return {"Mensaje": "Usuario encontrado", "Usuario": usuario}
        return {"Mensaje": f"No se encontro el id: {id}"}    
    else:
        return {"Mensaje": "No se proporciono un id"}

#endpoint con varios parametro opcionales
@app.get("/usuarios3/", tags=["3 parámetros opcionales"])
def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}