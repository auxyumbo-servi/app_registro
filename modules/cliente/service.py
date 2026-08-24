from models.cliente import Cliente
from modules.cliente.repository import ClienteRepository

repository = ClienteRepository

class ClienteService:

    def crear_cliente (nombre, contrato):

        cliente = Cliente(
            nombre=nombre,
            contrato=contrato
        )

        return repository.crear_cliente(cliente)

    def obtener_clientes():
        clientes = repository.obtener_clientes()
        opciones = {n.id: n.nombre
        for n in clientes
        }
        return repository.obtener_clientes

    def obtener_recipientes():
        return repository.obtener_recipientes

