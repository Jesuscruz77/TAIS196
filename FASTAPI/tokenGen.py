import jwt #type: ignore
from jwt import ExpiredSignatureError, InvalidTokenError #type: ignor
from fastapi import HTTPException #type: ignore

def createToken(datos: dict):
    token: str = jwt.encode(payload = datos, key = "secret", algorithm = "HS256")
    return token

def validateToken(token: str):
    try:
        data = jwt.decode(token,key="secret", algorithms=["HS256"])
        return data
    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token expiro")
    except InvalidTokenError:
        raise HTTPException(status_code=403, detail="Token no autorizado")