from nicegui import ui
from modules.cliente.controller import ClienteController

controller = ClienteController

class ClienteView:

    def cliente_view():


        with ui.card().classes("w-96"):

            nombre_input = ui.input(
                label="Nombre"
            ).classes("w-full")

            contrato_input = ui.input(
                label="Contrato"
            ).classes("w-full")

            def guardar_cliente():
                nombre = nombre_input.value
                contrato = contrato_input.value

                try:
                    controller.crear_cliente(
                        nombre,
                        contrato
                    )
                    ui.notify(
                        "Cliente guardado correctamente",
                        type="positive",
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
                        on_click=guardar_cliente,
                    ).classes("w-full")

            
            def recipiente():

                opciones = controller.obtener_recipientes()

                with ui.row().classes('w-full gap-4'):
                        
                                    recipiente_input = ui.select(
                                        options=opciones,
                                        label='Recipiente',
                                        with_input=True
                                    ).classes('flex-1')
                        
                                    cantidad_input = ui.number(
                                        label='Cantidad'
                                    ).classes('flex-1')
                        
                                    observacion_input = ui.input(
                                        label='Observación'
                                    ).classes('flex-1')


            recipiente()
            