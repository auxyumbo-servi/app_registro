from models.producto import Producto

from .producto_repository import (
    ProductoRepository,
)

from modules.base.service_generic import (
    GenericService,
)


class ProductoService(
    GenericService[Producto]
):
    repository = ProductoRepository