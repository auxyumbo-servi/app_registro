from nicegui import ui


def produccion_page():

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

            boton_guardar = ui.button(
                text="Guardar",
                on_click=None
            )


ui.run()