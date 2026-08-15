from pydantic import BaseModel
from datetime import date


class RegistroCreate(BaseModel):

    name: str

    quantity: int

    price: float

    expiration_date: date

    category: str