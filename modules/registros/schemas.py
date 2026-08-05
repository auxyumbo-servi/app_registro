from pydantic import BaseModel
from datetime import date


class ProductCreate(BaseModel):

    name: str

    quantity: int

    price: float

    expiration_date: date

    category: str