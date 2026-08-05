from nicegui import ui

from datetime import date

from .controllers import ProductController

from .components import product_table
from styles.buttons import *



controller = ProductController()


def registro_page():


    ui.label(
        "Registro de aforo"
    ).classes(
        "text-2xl"
    )

    dia = ui.date_input(
        "Fecha aforo"
    ).classes('flex-1')
    with ui.card().classes('w-full max-w-[1400px] p-6'):

        ui.label('Datos del aforo').classes(
            'text-h5 font-bold'
        )

        with ui.grid(columns=3).classes('w-full gap-4'):

            ui.input('Nombre')
            ui.input('Placa')
            ui.select(
                ['Empresa A', 'Empresa B'],
                label='Empresa'
            )

            ui.select(
                ['Normal', 'SyS'],
                label='Servicio'
            )

            ui.input('Fecha')

        # FILA 2: dos campos
        with ui.row().classes('w-full gap-4'):

            empresa = ui.select(
                ['Empresa 1', 'Empresa 2', 'Empresa 3'],
                label='Empresa'
            ).classes('flex-1')

            tipo_servicio = ui.select(
                ['Normal', 'SyS'],
                label='Tipo de servicio'
            ).classes('flex-1')

        # FILA 3: tres campos
        with ui.row().classes('w-full gap-4'):

            aforo = ui.input(
                label='Número de aforo'
            ).classes('flex-1')

            facturable = ui.select(
                ['Sí', 'No'],
                label='Facturable'
            ).classes('flex-1')

            observacion = ui.input(
                label='Observación'
            ).classes('flex-1')

            
    with ui.row().classes('w-full gap-4'):

        name = ui.input(
            "Nombre"
        ).classes('flex-1')

        aforo = ui.input(
            "Aforo"
        ).classes('flex-1')


    recipiente = ui.number(
        "Recipiente"
    )

    quantity = ui.number(
        "Cantidad"
    )



    category = ui.input(
        "Categoria"
    )


    table = ui.column()



    def load_table():

        table.clear()


        with table:

            product_table(
                controller.products()
            )



    def save():


        controller.save_product(

            name.value,

            int(quantity.value),

            float(recipiente.value),

            dia.value,

            category.value

        )


        # limpiar campos

        name.value=""

        quantity.value=None

        recipiente.value=None

        dia.value=None

        category.value=""




        load_table()



    primary("GUARDAR",save)


    load_table()