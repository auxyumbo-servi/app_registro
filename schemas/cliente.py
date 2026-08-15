from pydantic import BaseModel, EmailStr, Field


class ClienteCreate(BaseModel):
    nombre: str = Field(
        min_length=1,
        max_length=150,
    )

    contrato: str | None = None


class ClienteResponse(BaseModel):
    id: int
    nombre: str
    contrato: str | None

    model_config = {
        "from_attributes": True
    }
