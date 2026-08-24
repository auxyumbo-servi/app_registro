from nicegui import ui

from core.database import create_tables

from models.cliente import Cliente
from models.recipiente import Recipiente
from models.registro import Registro
from models.detalle_registro import DetalleRegistro

from modules.cliente.view import ClienteView

create_tables()

view = ClienteView

@ui.page('/')   
def cliente_view():
    view.cliente_view()

ui.run()