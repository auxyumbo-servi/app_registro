from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from models.base import BaseModel


class Cliente(BaseModel):

    __tablename__ = "clientes"


    nombre: Mapped[str]


    contrato: Mapped[str]


    registro: Mapped[list["Registro"]] = relationship(
        "Registro",
        back_populates="cliente"
    )