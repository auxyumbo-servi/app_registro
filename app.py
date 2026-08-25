from nicegui import ui

from core.database import create_tables

from models.cliente import Cliente
from models.recipiente import Recipiente
from models.registro import Registro
from models.detalle_registro import DetalleRegistro

from modules.cliente.view import ClienteView
from modules.recipiente.view import RecipienteView
from modules.registro.view import RegistroView

create_tables()


@ui.page('/')   
def cliente_view():
    view = ClienteView
    view.cliente_view()

@ui.page('/recipientes')   
def recipientes_view():
    view = RecipienteView
    view.recipiente_view()

@ui.page('/registros')   
def registro_view():
    view = RegistroView
    view.registro_view()

ui.run()