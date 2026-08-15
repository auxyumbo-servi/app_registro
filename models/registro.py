<<<<<<< HEAD
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


if TYPE_CHECKING:
    from models.cliente import Cliente
    from models.detalle_registro import DetalleRegistro


class Registro(Base):
    __tablename__ = "registro"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    cliente_id: Mapped[int] = mapped_column(
        ForeignKey("cliente.id"),
        nullable=False,
    )

    fecha: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    cliente: Mapped["Cliente"] = relationship(
        back_populates="registros",
    )

    detalles: Mapped[list["DetalleRegistro"]] = relationship(
        back_populates="registro",
        cascade="all, delete-orphan",
    )
=======
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
>>>>>>> a3eebcbd984da44ca6944e417986a7df90031583
