from models.producto import Producto

from modules.base.repository_generic import (
    GenericRepository,
)


class ProductoRepository(
    GenericRepository[Producto]
):
    model = Producto