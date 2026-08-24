from modules.cliente.service import ClienteService

service = ClienteService

class ClienteController:

    def crear_cliente(nombre, contrato):
        return service.crear_cliente(
            nombre,
            contrato
        )

    def obtener_clientes():
        return
    service.obtener_clientes()
    
    def obtener_recipientes():
        return
    service.obtener_recipientes()