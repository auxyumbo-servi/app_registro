<<<<<<< HEAD
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
=======
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import ForeignKey

from models.base import BaseModel


class DetalleRegistro(BaseModel):

    __tablename__ = "detella_registro"
    #registro_id--> models/registro
    registro_id: Mapped[int] = mapped_column(
        ForeignKey(
            "registro.id"
        )
    )
    #recipiente --> models/recipiente
    recipiente: Mapped[int]

    cantidad: Mapped[float]#detalle

    observacion: Mapped[str]#detalle


    registros: Mapped["Registro"] = relationship(
        "Registro",
        back_populates="detalles"
    )




>>>>>>> a3eebcbd984da44ca6944e417986a7df90031583
