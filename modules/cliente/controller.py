from modules.cliente.service import ClienteService

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
    def opciones_clientes():
        return ClienteService.obtener_opciones()

    @staticmethod
    def obtener_cliente(cliente_id):
        return ClienteService.obtener_cliente(cliente_id)
