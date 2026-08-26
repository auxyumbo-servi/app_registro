from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base


class Producto(Base):

    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    nombre: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    precio: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )