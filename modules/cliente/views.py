from nicegui import ui

from core.database import get_session
from modules.cliente.service import crear_cliente
from schemas.cliente import ClienteCreate
from styles.header import header
from styles.footer import navbar


def cliente_view(): 
    header('Registro de Cliente')


    with ui.card().classes("w-96"):

        nombre = ui.input(
            label="Nombre"
        ).classes("w-full")

        contrato = ui.input(
            label="Contrato"
        ).classes("w-full")

        resultado = ui.label()

        def guardar():

            try:
                # 1. Validar los datos con Pydantic
                data = ClienteCreate(
                    nombre=nombre.value,
                    contrato=contrato.value,
                )
                

                # 2. Abrir sesión
                with get_session() as session:

                    # 3. Guardar mediante el service
                    cliente = crear_cliente(
                        session,
                        data,
                    )

                resultado.set_text(
                    f"Cliente {cliente.id} creado correctamente"
                )

                ui.notify(
                    "Cliente guardado correctamente",
                    type="positive",
                )

                # Limpiar formulario
                nombre.value = ""
                contrato.value = ""

            except Exception as e:

                ui.notify(
                    str(e),
                    type="negative",
                )

        ui.button(
            "Guardar Cliente",
            on_click=guardar,
        ).classes("w-full")


    navbar()