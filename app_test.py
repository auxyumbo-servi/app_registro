from nicegui import ui

from core.database import create_tables


from modules.detalle_pedido.view import Pedidoview
from modules.producto.producto_view import ProductoView
from modules.usuario.usuario_view import UsuarioView



@ui.page('/')
def pedidos():
    view = Pedidoview
    view.pedido_view()

@ui.page('/p')
def productos():
    view =ProductoView
    view.producto_view()

@ui.page('/a')
def usuarios():
    view =UsuarioView
    view.usuario_view()

create_tables()

ui.run()

#hola