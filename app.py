from nicegui import ui

from core.database import create_tables

from modules.products.views import products_page
from modules.registros.views import registro_page
from modules.produccion.views import produccion_page
from modules.cliente.views import cliente_page


create_tables()



ui.page("/")(
    products_page
)
ui.page("/registros")(
    registro_page
)
ui.page("/produccion")(
    produccion_page
)
ui.page("/cliente")(
    cliente_page
)