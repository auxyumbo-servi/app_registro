from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base


if TYPE_CHECKING:
    from models.registro import Registro


class Cliente(Base):
    __tablename__ = "cliente"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    nombre: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    contrato: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    registros: Mapped[list["Registro"]] = relationship(
        back_populates="cliente",
        cascade="all, delete-orphan",
    )
