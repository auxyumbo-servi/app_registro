from decimal import Decimal

from pydantic import BaseModel, Field


class RecipienteCreate(BaseModel):
    nombre: str = Field(
        min_length=1,
        max_length=150,
    )

    equivalencia: Decimal = Field(
        ge=0,
    )

class RecipienteResponse(BaseModel):
    id: int
    nombre: str
    equivalencia: Decimal
    model_config = {
        "from_attributes": True
    }
