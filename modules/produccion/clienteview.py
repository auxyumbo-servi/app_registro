from nicegui import ui
from .clientecontroller import ClienteController

class ClienteView:
    @staticmethod
    def cliente_view():

        controller = ClienteController()

        nombre_input = ui.input(label='nombre')

        contrato_input = 'Default-00001'

        ui.label('Hola mundo').classes('H1')
        pass

        def guardar():
            nombre = nombre_input.value
            contrato = contrato_input

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
                
                
            except Exception as e:
                
                ui.notify(
                    str(e),
                    type="negative",
                )
        ui.button(
                    "Guardar Cliente",
                    on_click=guardar,
                ).classes("w-full")