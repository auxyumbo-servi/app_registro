from models.cliente import Cliente

from .repository_generic import GenericRepository


class ClienteRepository(GenericRepository[Cliente]):

    model = Cliente 