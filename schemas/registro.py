from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class RegistroDetalleCreate(BaseModel):
    producto_id: int

    cantidad: int = Field(
        gt=0,
    )


class RegistroCreate(BaseModel):
    cliente_id: int

    detalles: list[RegistroDetalleCreate] = Field(
        min_length=1,
    )


class RegistroResponse(BaseModel):
    id: int
    cliente_id: int
    fecha: datetime

    model_config = {
        "from_attributes": True
    }
