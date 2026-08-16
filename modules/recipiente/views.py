from nicegui import ui

from core.database import get_session
from modules.recipiente.service import crear_recipiente
from schemas.recipiente import RecipienteCreate
from styles.header import header
from styles.footer import navbar


def recipiente_view(): 
    header('Registro de Recipiente')


    with ui.card().classes("w-96"):

        nombre = ui.input(
            label="Nombre"
        ).classes("w-full")

        equivalencia = ui.input(
            label="Equivalencia"
        ).classes("w-full")

        resultado = ui.label()

        def guardar():

            try:
                # 1. Validar los datos con Pydantic
                data = RecipienteCreate(
                    nombre=nombre.value,
                    equivalencia=equivalencia.value,
                )
                

                # 2. Abrir sesión
                with get_session() as session:

                    # 3. Guardar mediante el service
                    recipiente = crear_recipiente(
                        session,
                        data,
                    )

                resultado.set_text(
                    f"Recipiente {recipiente.id} creado correctamente"
                )

                ui.notify(
                    "Recipiente guardado correctamente",
                    type="positive",
                )

                # Limpiar formulario
                nombre.value = ""
                equivalencia.value = ""

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