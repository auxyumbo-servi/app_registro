from nicegui import ui

from schemas.helper import procesar_tab


@ui.page("/")
def usuario_view():
    nombre = ui.input("Campo")

    id_input = ui.number(
        label="ID del usuario",
        min=1,
        precision=0,
    )
    date = ui.input(
        label="Fecha"
    )
    def obtener_por_id():
        print("Buscando usuario...")

    def crear():
        print("Creando usuario...")

    nombre.on(
        "keydown",
        lambda e: procesar_tab(
            e,
            campo_origen=nombre,
            campo_destino=date,
            funcion_1=obtener_por_id,
            funcion_2=crear,
            tiempo=.5,
        )
    )


ui.run()