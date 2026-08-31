from models.cliente import Cliente
from modules.cliente.repository import ClienteRepository


class ClienteService:

    repository = ClienteRepository()

    @staticmethod
    def crear_cliente(nombre, contrato):
        
        if not nombre:
            raise ValueError ('Nombre Obligatorio')

        cliente = Cliente(
            nombre=nombre,
            contrato=contrato
        )
        return ClienteService.repository.crear_cliente(cliente)

    @staticmethod
    def obtener_clientes():
        return ClienteService.repository.obtener_clientes()

    @staticmethod
    def obtener_opciones():
        clientes = ClienteService.repository.obtener_clientes()

        return {
            n.id: n.nombre
            for n in clientes
        }

    @staticmethod
    def obtener_cliente(cliente_id):
        return ClienteService.repository.obtener_cliente(cliente_id)

