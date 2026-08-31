from sqlalchemy import ForeignKey, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base


class DetallePedido(Base):

    __tablename__ = "detalles_pedido"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    pedido_id: Mapped[int] = mapped_column(
        ForeignKey("pedidos.id"),
        nullable=False,
    )

    producto_id: Mapped[int] = mapped_column(
        ForeignKey("productos.id"),
        nullable=False,
    )

    cantidad: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    precio: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    pedido: Mapped["Pedido"] = relationship(
        "Pedido",
        back_populates="detalles",
    )

    producto: Mapped["Producto"] = relationship(
        "Producto",
    )