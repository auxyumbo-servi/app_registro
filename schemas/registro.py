from pydantic import BaseModel, EmailStr, Field


class RegistroCreate(BaseModel):
    nombre: str = Field(
        min_length=1,
        max_length=150,
    )

    placa: str | None = None
    




class RegistroResponse(BaseModel):
    id: int
    nombre: str
    placa: str | None

    model_config = {
        "from_attributes": True
    }
