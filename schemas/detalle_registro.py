from decimal import Decimal

from pydantic import BaseModel, Field


class DetalleRegistroCreate(BaseModel):
    registro_id: int
    recipiente_id: int

    cantidad: int = Field(
        gt=0,
    )

    precio_unitario: Decimal = Field(
        ge=0,
    )


class DetalleRegistroResponse(BaseModel):
    id: int
    registro_id: int
    recipiente_id: int
    cantidad: int
    precio_unitario: Decimal
    subtotal: Decimal

    model_config = {
        "from_attributes": True
    }
