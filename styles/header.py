from nicegui import ui

<<<<<<< HEAD
def header(titulo):
=======
def header(text):
>>>>>>> a3eebcbd984da44ca6944e417986a7df90031583
    with ui.header().props(
        """
        elevated
        bordered
        """
    ).classes('bg-yellow-300 text-black'):

<<<<<<< HEAD
        ui.label(text=titulo).classes('text-h4 font-bold')
=======
        ui.label(text=text)
>>>>>>> a3eebcbd984da44ca6944e417986a7df90031583
