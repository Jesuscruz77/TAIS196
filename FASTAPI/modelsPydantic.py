from pydantic import BaseModel, Field  # type: ignore

class modelUsuario (BaseModel):
    id: int = Field(..., gt=0, description="Id unico y numeros positivos")
    nombre: str = Field(..., min_length=3, max_length=15, description="Nombre debe contener solo letras y espacios")
    edad: int = Field(..., gt=0, lt=130, description="La edad debe ser mayor que 0 y menor que 130")
    correo: str = Field(..., pattern="^[\w\.-]+@[\w\.-]+\.\w+$", description="Correo electronico valido", example="jesus@gmail.com")