from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


<<<<<<< HEAD
if TYPE_CHECKING:
    from models.registro import Registro
=======
class Cliente(BaseModel):

    __tablename__ = "clientes"
>>>>>>> a3eebcbd984da44ca6944e417986a7df90031583


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

<<<<<<< HEAD
    registros: Mapped[list["Registro"]] = relationship(
        back_populates="cliente",
        cascade="all, delete-orphan",
    )
=======
    registro: Mapped[list["Registro"]] = relationship(
        "Registro",
        back_populates="cliente"
    )
>>>>>>> a3eebcbd984da44ca6944e417986a7df90031583
