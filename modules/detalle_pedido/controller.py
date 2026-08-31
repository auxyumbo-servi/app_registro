from models.pedido import Pedido

from modules.base.controller_generic import (
    GenericController,
)

from .service import (
    PedidoService,
)


class PedidoController(
    GenericController[Pedido]
):

    service = PedidoService

    @classmethod
    def crear_con_detalles(
        cls,
        usuario_id: int,
        detalles: list[dict],
    ) -> Pedido:

        return cls.service.crear_con_detalles(
            usuario_id,
            detalles,
        )