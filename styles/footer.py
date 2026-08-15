from nicegui import ui


MENU = [
    ('INICIO', '/'),
    ('AFOROS', '/aforos'),
    ('CLIENTES', '/clientes'),
    ('TARIFAS', '/tarifas'),
    
]


def navbar():

    with ui.footer().classes('bg-yellow-300 p-0'):

        with ui.row().classes(
            'w-full justify-center gap-0'
        ):

            for nombre, ruta in MENU:

                ui.button(
                    nombre,
                    on_click=lambda r=ruta: ui.navigate.to(r)
                ).props(
                    'flat'
                ).classes(
                    'text-black px-5 py-4'
                )