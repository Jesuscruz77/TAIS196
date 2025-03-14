from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional, List
from modelsenv import modelEnvios


app = FastAPI(
    title="Examen con fastAPI",
    description="Segundo parcial",
    version="1.0.1"
)


envios = [
    {"cp": "76720", "Destino": "Pedro Escobedo", "peso": 5, },
    {"cp": "76710", "Destino": "Queretaro", "peso": 4, },
    {"cp": "76730", "Destino": "Tequisquiapan", "peso": 6, }
]

@app.get("/envios", response_model = List[modelEnvios] , tags=["Envios"])
def consultarenvios():
    return envios


@app.post("/envios/", response_model = modelEnvios,tags=["Envios"])
def crearenvio(envio:modelEnvios):
    for env in envios:
        if env["cp"] == envio.cp:
            raise HTTPException(status_code=400, detail="El envio ya existe")
    envios.append(envio.dict())
    return envio

@app.delete("/envios/{cp}",response_model = modelEnvios, tags=["Envios"])
def eliminarenvio(cp: str):
    for index, envio in enumerate(envios):
        if envio["cp"] == cp:
            eliminae = envios.pop(index)
            return eliminae
    raise HTTPException(status_code=404, detail="El envio no existe")
      


