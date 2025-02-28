import jwt #type: ignore

def createToken(datos: dict):
    token: str = jwt.encode(payload = datos, key = "secret", algorithm = "HS256")
    return token