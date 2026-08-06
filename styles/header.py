from nicegui import ui

def header(text):
    with ui.header().props(
        """
        elevated
        bordered
        """
    ).classes('bg-yellow-300 text-black'):

        ui.label(text=text)
