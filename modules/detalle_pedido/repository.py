from sqlalchemy import select
from sqlalchemy.orm import selectinload

from core.database import SessionLocal
from models.pedido import Pedido

from modules.base.repository_generic import (
    GenericRepository,
)


class PedidoRepository(
    GenericRepository[Pedido]
):

    model = Pedido

    @classmethod
    def obtener_con_detalles(
        cls,
        pedido_id: int,
    ) -> Pedido | None:

        with SessionLocal() as session:

            stmt = (
                select(cls.model)
                .options(
                    selectinload(
                        cls.model.detalles
                    )
                )
                .where(
                    cls.model.id == pedido_id
                )
            )

            return session.scalars(
                stmt
            ).first()