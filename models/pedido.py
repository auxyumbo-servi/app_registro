from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base


class Pedido(Base):

    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id"),
        nullable=False,
    )

    fecha: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
    )

    usuario: Mapped["Usuario"] = relationship(
        "Usuario",
        back_populates="pedidos",
    )

    detalles: Mapped[list["DetallePedido"]] = relationship(
        "DetallePedido",
        back_populates="pedido",
        cascade="all, delete-orphan",
    )