from nicegui import ui
from modules.cliente.controller import ClienteController
from styles.footer import navbar

#registro


class ClienteView:
    @staticmethod
    def registro_view():

        controller = ClienteController()

        with ui.card().classes("w-96"):

            nombre_input = ui.input(
                label="Nombre"
            ).classes("w-full")

            contrato_input = ui.input(
                label="Contrato"
            ).classes("w-full")

            def guardar_registro():
                nombre = nombre_input.value
                contrato = contrato_input.value

                try:
                    controller.crear_cliente(
                        nombre,
                        contrato
                    )
                    ui.notify(
                        "Cliente sguardado correctamente",
                        type="poitive",
                    )

                    # Limpiar formulario
                    nombre_input.value = ""
                    contrato_input.value = ""
                    
                    
                except Exception as e:
                    
                    ui.notify(
                        str(e),
                        type="negative",
                    )
            ui.button(
                        "Guardar Cliente",
                        on_click=guardar_registro,
                    ).classes("w-full")

            
            def recipiente():
                controller = ClienteController()

                opciones = controller.opciones_clientes()


                with ui.row().classes('w-full gap-4'):
                        
                                    cliente = ui.select(
                                    options=opciones,
                                    with_input=True,
                                    label='cliente'
                                    ).props('use-input')
                                        
                                    cantidad_input = ui.number(
                                        label='Cantidad'
                                    ).classes('flex-1')

                                    observacion_input = ui.input(
                                        label='Observación'
                                    ).classes('flex-1')


            recipiente()
        navbar()