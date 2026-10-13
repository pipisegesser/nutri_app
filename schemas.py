from pydantic import BaseModel
from typing import Optional

class PacienteBase(BaseModel):
    nombre: str
    apellido: str
    edad: int
    email: str
    telefono: Optional[str] = None
    objetivo: Optional[str] = None

class PacienteCreate(PacienteBase):
    pass

class PacienteResponse(PacienteBase):
    id: int

    class Config:
        from_attributes = True