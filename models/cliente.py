from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from models.base import BaseModel


class Usuario(BaseModel):

    __tablename__ = "usuarios"


    nombre: Mapped[str]


    contrato: Mapped[str]


    transacciones: Mapped[list["Transaccion"]] = relationship(
        "Transaccion",
        back_populates="usuario"
    )