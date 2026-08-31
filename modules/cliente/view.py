from nicegui import ui
from modules.cliente.controller import ClienteController
from styles.footer import navbar
import time



class ClienteView:
    @staticmethod
    def cliente_view():

        controller = ClienteController()

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
                        on_click=guardar_cliente,
                    ).classes("w-full")
        navbar()