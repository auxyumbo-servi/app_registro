from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date

from datetime import date

from models.base import Base

if TYPE_CHECKING:
    from models.cliente import Cliente

class Tarifa(Base):

    __tablename__ = "products"


    id: Mapped[int] = mapped_column(primary_key=True,
                                    autoincrement=True,
                                    )
    

