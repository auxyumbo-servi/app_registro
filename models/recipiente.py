from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


if TYPE_CHECKING:
    from models.detalle_registro import DetalleRegistro


class Recipiente(Base):
    __tablename__ = "recipiente"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    nombre: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    equivalencia: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    detalles: Mapped[list["DetalleRegistro"]] = relationship(
        back_populates="recipiente",
    )
