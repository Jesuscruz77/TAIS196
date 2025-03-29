from fastapi.responses import JSONResponse  # type: ignore
from modelsPydantic import  modelAuth
from tokenGen import createToken
from fastapi import APIRouter # sirve para importar la clase APIRouter

routerAuth = APIRouter() # se crea una instancia de la clase APIRouter

@routerAuth.post("/auth", tags=["Autenticacion"])
def login(autorizado: modelAuth):
    if autorizado.correo == "jesus@example.com" and autorizado.contrasena == "123456789":
        token:str = createToken(autorizado.model_dump())
        return JSONResponse(content= token)
    else: 
        return {"Aviso": "Usuario no autorizado"}