from pydantic import BaseModel
from datetime import date


class ProductCreate(BaseModel):

    name: str

    quantity: str

    price: float

    expiration_date: date

    category: str