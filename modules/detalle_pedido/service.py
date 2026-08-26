from datetime import datetime

from models.pedido import Pedido
from models.detalle_pedido import DetallePedido

from .repository import (
    PedidoRepository,
)


class PedidoService:

    repository = PedidoRepository

    @classmethod
    def crear_con_detalles(
        cls,
        usuario_id: int,
        detalles: list[dict],
    ) -> Pedido:

        pedido = Pedido(
            usuario_id=usuario_id,
        )

        for detalle_data in detalles:

            detalle = DetallePedido(
                producto_id=detalle_data["producto_id"],
                cantidad=detalle_data["cantidad"],
                precio=detalle_data["precio"],
            )

            pedido.detalles.append(detalle)

        return cls.repository.crear(
            pedido
        )