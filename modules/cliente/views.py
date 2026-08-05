#views
from nicegui import ui
from styles.buttons import primary
from styles.header import header


@ui.page("/inicio")
def cliente_page():

    header()
    ui.label("Clientes")

    primary(
        "Guardar",
        lambda: print("guardar")
    )