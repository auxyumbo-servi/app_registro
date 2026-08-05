# main.py

from nicegui import ui

from modules.cliente.views import cliente_page
from modules.registros.views import registro_page


ui.page("/inicio")(cliente_page)
ui.page("/registros")(registro_page)



ui.run()