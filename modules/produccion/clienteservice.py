from models.cliente import Cliente
from .clienterepository import ClienteRepository


class ClienteService:

    @staticmethod
    def crear_cliente(nombre, contrato):

        cliente = Cliente(
            nombre=nombre,
            contrato=contrato
        )

        return ClienteRepository.crear(cliente)

    @staticmethod
    def obtener_clientes():

        return ClienteRepository.obtener_todos()

    @staticmethod
    def obtener_cliente(cliente_id: int):

        return ClienteRepository.obtener_por_id(
            cliente_id
        )

    @staticmethod
    def actualizar_cliente(
        cliente_id: int,
        datos: dict
    ):

        return ClienteRepository.actualizar(
            cliente_id,
            datos
        )

    @staticmethod
    def eliminar_cliente(cliente_id: int):

        return ClienteRepository.eliminar(
            cliente_id
        )