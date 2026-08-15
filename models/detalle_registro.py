from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


if TYPE_CHECKING:
    from models.registro import Registro
    from models.recipiente import Recipiente


class DetalleRegistro(Base):
    __tablename__ = "detalle_registro"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    registro_id: Mapped[int] = mapped_column(
        ForeignKey("registro.id"),
        nullable=False,
    )

    recipiente_id: Mapped[int] = mapped_column(
        ForeignKey("recipiente.id"),
        nullable=False,
    )

    cantidad: Mapped[int] = mapped_column(
        nullable=False,
    )

    precio_unitario: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    subtotal: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    registro: Mapped["Registro"] = relationship(
        back_populates="detalles",
    )

    recipiente: Mapped["Recipiente"] = relationship(
        back_populates="detalles",
    )
