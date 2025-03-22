from pydantic import BaseModel, Field, EmailStr # type: ignore

class modelUsuario (BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Nombre debe contener solo letras y espacios")
    age: int = Field(..., gt=0, lt=130, description="La edad debe ser mayor que 0 y menor que 130")
    email: str = Field(..., pattern="^[\w\.-]+@[\w\.-]+\.\w+$", description="Correo electronico valido", example="jesus@gmail.com")

class modelAuth(BaseModel):
    correo: EmailStr
    contrasena: str = Field(..., min_length=8, strip_whitespace=True, description="password incorrecto - min 8 caracteres")