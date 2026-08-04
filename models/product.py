from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date

from datetime import date

from .base import BaseModel


class Product(BaseModel):

    __tablename__ = "products"


    name: Mapped[str]


    quantity: Mapped[int]


    price: Mapped[float]


    expiration_date: Mapped[date] = mapped_column(
        Date
    )


    category: Mapped[str]