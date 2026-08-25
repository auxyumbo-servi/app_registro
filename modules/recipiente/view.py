from nicegui import ui
from modules.recipiente.controller import RecipienteController
from styles.footer import navbar

class RecipienteView:
    @staticmethod    

    def recipiente_view():

        controller = RecipienteController()

        with ui.card().classes("w-96"):

            nombre_input = ui.input(
                label="Nombre"
            ).classes("w-full")

            equivalencia_input = ui.number(
                label="Equivalencia"
            ).classes("w-full")


            def guardar():
                nombre = nombre_input.value
                equivalencia = equivalencia_input.value

                try:
                    controller.crear_recipiente(
                        nombre,
                        equivalencia
                    )

                    ui.notify(
                        "Recipiente guardado correctamente",
                        type="positive",
                    )

                    # Limpiar formulario
                    nombre_input.value = ""
                    equivalencia_input.value = ""

                except Exception as e:

                    ui.notify(
                        str(e),
                        type="negative",
                    )

            ui.button(
                "Guardar Recipiente",
                on_click=guardar,
            ).classes("w-full")


        navbar()