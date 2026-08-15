from pydantic import BaseModel
from datetime import date


class DetalleCreate(BaseModel):

    registro_id: int

    recipiente: str

    cantidad: int

    observacion: str
