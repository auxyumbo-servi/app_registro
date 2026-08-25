from .clienteservice import ClienteService


class ClienteController:

    @staticmethod
    def crear_cliente(nombre, contrato):

        return ClienteService.crear_cliente(
            nombre,
            contrato
        )

    @staticmethod
    def clientes():

        return ClienteService.obtener_clientes()

    @staticmethod
    def obtener_cliente(cliente_id):

        return ClienteService.obtener_cliente(
            cliente_id
        )

    @staticmethod
    def actualizar_cliente(
        cliente_id,
        datos
    ):

        return ClienteService.actualizar_cliente(
            cliente_id,
            datos
        )

    @staticmethod
    def eliminar_cliente(cliente_id):

        return ClienteService.eliminar_cliente(
            cliente_id
        )