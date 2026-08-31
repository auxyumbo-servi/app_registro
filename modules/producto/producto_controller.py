from models.producto import Producto

from modules.base.controller_generic import (
    GenericController,
)

from .producto_service import (
    ProductoService,
)


class ProductoController(
    GenericController[Producto]
):
    service = ProductoService