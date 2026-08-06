from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey

from datetime import date

from .base import BaseModel


class Registro(BaseModel):

    __tablename__ = "registros"

    fecha: Mapped[date] = mapped_column(
        Date
    )
    #nombre_id --> models/cliente
    nombre_id: Mapped[int] = mapped_column(
        ForeignKey(
            "cliente.id"
        )
    )

    aforo: Mapped[str]
    

    cliente: Mapped["Cliente"] = relationship(
        "Cliente",
        back_populates="registro"
    )

    detalles: Mapped["DetalleRegistro"] = relationship(
            "DetalleRegistro",
            back_populates="registros"
        )