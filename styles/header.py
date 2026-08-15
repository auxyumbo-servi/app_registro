from nicegui import ui

def header(titulo):
    with ui.header().props(
        """
        elevated
        bordered
        """
    ).classes('bg-yellow-300 text-black'):

        ui.label(text=titulo).classes('text-h4 font-bold')
