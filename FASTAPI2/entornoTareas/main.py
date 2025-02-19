from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="API de Gestión de Tareas (To-Do List)",
    description="Jesús Cruz",
    version="1.0.1"
) 

tareas = [
    {"id": 1, "titulo": "Estudiar para el examen", "descripcion": "Repasar los apuntes de TAI", "vencimiento": "14-02-25", "estado": "Completada"},
    {"id": 2, "titulo": "Entregar avance de Enpoint", "descripcion": "Registrar avances en GitHub", "vencimiento": "14-02-25", "estado": "Completada"},
    {"id": 3, "titulo": "Hacer Enpoint de obtener datos", "descripcion": "Crear un endpoint con el metodo GET", "vencimiento": "16-02-25", "estado": "Pendiente"},
    {"id": 4, "titulo": "Hacer Enpoint de agregar datos", "descripcion": "Crear un endpoint con el metodo POST", "vencimiento": "17-02-25", "estado": "Pendiente"},
    {"id": 5, "titulo": "Hacer Enpoint de actualizar datos", "descripcion": "Crear un endpoint con el metodo PUT", "vencimiento": "18-02-25", "estado": "Pendiente"},
    {"id": 6, "titulo": "Hacer Enpoint de eliminar datos", "descripcion": "Crear un endpoint con el metodo DELETE", "vencimiento": "19-02-25", "estado": "Pendiente"}
]



#Endpoint para consultar todas las tareas
@app.get("/tareas", tags=["Obtener Tareas"])
def ConsultarTodos():
    return {"Tareas Registradas": tareas}

#Endpoint para agregar una tarea nueva
@app.post("/tareas/", tags=["Crear una nueva tarea"])
def AgregarTarea(tarea: dict):
    for tar in tareas:
        if tar["id"] == tarea.get("id"):
            raise HTTPException(status_code=400, detail="El id de la tarea ya esta registrado")
        
    tareas.append(tarea)
    return tarea

#Endpoint para actualizar una tarea
@app.put("/tareas/{id}", tags=["Actualizar una tarea"])
def ActualizarTarea(id: int, tarea: dict):
    for index,tar in enumerate(tareas):
        if tar["id"] == id:
            tareas[index].update(tarea)
            return tareas[index]
    raise HTTPException(status_code=404, detail="El id de la tarea no esta registrado")

#Endpoint para eliminar una tarea
@app.delete("/tareas/{id}", tags=["Eliminar una tarea"])
def EliminarTarea(id: int):
    for index,tar in enumerate(tareas):
        if tar["id"] == id:
            tareas.pop(index)
            return {"Mensaje": "Tarea eliminada"}
    raise HTTPException(status_code=404, detail="El id de la tarea no esta registrado")

