from fastapi import FastAPI2, HTTPException
from typing import Optional

app = FastAPI2(
    title="API de Gestión de Tareas (To-Do List)",
    description="Jesús Cruz",
    version="1.0.1"
) 

tareas = [
    {"id": 1, "titulo": "Estudiar para el examen", "descripcion": "Repasar los apuntes de TAI", "vencimiento": "14-02-24", "estado": "Completada"},
]
