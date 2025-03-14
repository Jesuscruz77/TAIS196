from pydantic import BaseModel, Field

class modelEnvios(BaseModel):
    cp: str = Field(..., min_length=5, description="El codigo postal debe tener minimo 5 caracteres")
    Destino: str = Field(..., min_length=6, description="El destino debe tener minimo 6 caracteres")
    peso: int = Field(..., gt=0,  lt=500,description="El peso debe ser mayor a 0 y menor a 500")