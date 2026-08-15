from decimal import Decimal

from nicegui import ui

from core.database import get_session
from schemas.registro import (
    RegistroCreate,
    RegistroDetalleCreate,
)
from modules.registro.service import crear_registro


def registro_view():

    ui.label("Nuevo Registro").classes("text-h4")

    cliente_id = ui.number(
        label="Cliente ID",
        min=1,
    )

    detalles = []

    producto_id = ui.number(
        label="Producto ID",
        min=1,
    )

    cantidad = ui.number(
        label="Cantidad",
        min=1,
        value=1,
    )

    def guardar():

        try:

            data = RegistroCreate(
                cliente_id=int(cliente_id.value),
                detalles=[
                    RegistroDetalleCreate(
                        producto_id=int(producto_id.value),
                        cantidad=int(cantidad.value),
                    )
                ],
            )

            with get_session() as session:

                registro = crear_registro(
                    session,
                    data,
                )

            ui.notify(
                f"Registro {registro.id} creado"
            )

        except ValueError as e:

            ui.notify(
                str(e),
                type="negative",
            )

    ui.button(
        "Guardar",
        on_click=guardar,
    )
