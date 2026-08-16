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
