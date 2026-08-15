from pydantic import BaseModel
from datetime import date


class RegistroCreate(BaseModel):

    fecha: date

    nombre: str

    aforo: str

