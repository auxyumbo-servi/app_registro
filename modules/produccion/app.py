from nicegui import ui

from ...core.database import create_tables

from models.cliente import Cliente

from clienteview import ClienteView


@ui.page('/')   
def cliente_view():
    view = ClienteView
    view.cliente_view()

create_tables()

ui.run()