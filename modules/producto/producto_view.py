from nicegui import ui

from .producto_controller import ProductoController
from models.producto import Producto

class ProductoView:
    @ui.page("/productos")
    def producto_view():

        ui.label("Gestión de Productos").classes(
            "text-2xl font-bold mb-4"
        )

        # ==========================================================
        # CAMPOS DEL FORMULARIO
        # ==========================================================

        with ui.row().classes("items-end"):

            nombre_input = ui.input(
                label="Nombre"
            )

            precio_input = ui.number(
                label="Precio",
                min=0,
                precision=2,
            )

        # ==========================================================
        # TABLA
        # ==========================================================

        tabla = ui.table(
            columns=[
                {
                    "name": "id",
                    "label": "ID",
                    "field": "id",
                    "align": "left",
                },
                {
                    "name": "nombre",
                    "label": "Nombre",
                    "field": "nombre",
                },
                {
                    "name": "precio",
                    "label": "Precio",
                    "field": "precio",
                },
            ],
            rows=[],
            row_key="id",
        ).classes("w-full")

        # ==========================================================
        # CARGAR PRODUCTOS
        # ==========================================================

        def cargar_productos():

            productos = ProductoController.listar()

            tabla.rows = [
                {
                    "id": producto.id,
                    "nombre": producto.nombre,
                    "precio": producto.precio,
                }
                for producto in productos
            ]

            tabla.update()

        # ==========================================================
        # CREAR
        # ==========================================================

        def crear():

            nombre = nombre_input.value
            precio = precio_input.value

            if not nombre:
                ui.notify(
                    "El nombre es obligatorio",
                    type="warning",
                )
                return

            if precio is None:
                ui.notify(
                    "El precio es obligatorio",
                    type="warning",
                )
                return

            try:

                producto = Producto(
                    nombre=nombre,
                    precio=precio,
                )

                ProductoController.crear(producto)

                ui.notify(
                    "Producto creado correctamente",
                    type="positive",
                )

                nombre_input.value = ""
                precio_input.value = None

                cargar_productos()

            except Exception as error:

                ui.notify(
                    f"Error al crear: {error}",
                    type="negative",
                )

        # ==========================================================
        # OBTENER POR ID
        # ==========================================================

        def obtener_por_id():

            try:

                producto_id = int(id_input.value)

                producto = ProductoController.obtener(
                    producto_id
                )

                if producto is None:

                    ui.notify(
                        "Producto no encontrado",
                        type="warning",
                    )

                    return

                nombre_input.value = producto.nombre
                precio_input.value = producto.precio

                ui.notify(
                    f"Producto encontrado: {producto.nombre}",
                    type="positive",
                )

            except (TypeError, ValueError):

                ui.notify(
                    "Ingrese un ID válido",
                    type="warning",
                )

        # ==========================================================
        # ACTUALIZAR
        # ==========================================================

        def actualizar():

            try:

                producto_id = int(id_input.value)

                datos = {
                    "nombre": nombre_input.value,
                    "precio": precio_input.value,
                }

                producto = ProductoController.actualizar(
                    producto_id,
                    datos,
                )

                if producto is None:

                    ui.notify(
                        "Producto no encontrado",
                        type="warning",
                    )

                    return

                ui.notify(
                    "Producto actualizado correctamente",
                    type="positive",
                )

                cargar_productos()

            except (TypeError, ValueError):

                ui.notify(
                    "Ingrese un ID válido",
                    type="warning",
                )

            except Exception as error:

                ui.notify(
                    f"Error al actualizar: {error}",
                    type="negative",
                )

        # ==========================================================
        # ELIMINAR
        # ==========================================================

        def eliminar():

            try:

                producto_id = int(id_input.value)

                eliminado = ProductoController.eliminar(
                    producto_id
                )

                if not eliminado:

                    ui.notify(
                        "Producto no encontrado",
                        type="warning",
                    )

                    return

                ui.notify(
                    "Producto eliminado correctamente",
                    type="positive",
                )

                nombre_input.value = ""
                precio_input.value = None

                cargar_productos()

            except (TypeError, ValueError):

                ui.notify(
                    "Ingrese un ID válido",
                    type="warning",
                )

            except Exception as error:

                ui.notify(
                    f"Error al eliminar: {error}",
                    type="negative",
                )

        # ==========================================================
        # OPERACIONES POR ID
        # ==========================================================

        with ui.row().classes("items-end mt-4"):

            id_input = ui.number(
                label="ID del producto",
                min=1,
                precision=0,
            )

            ui.button(
                "Buscar",
                on_click=obtener_por_id,
            )

            ui.button(
                "Actualizar",
                on_click=actualizar,
            )

            ui.button(
                "Eliminar",
                on_click=eliminar,
                color="negative",
            )

        # ==========================================================
        # BOTONES
        # ==========================================================

        with ui.row().classes("mt-4"):

            ui.button(
                "Crear producto",
                on_click=crear,
                color="primary",
            )

            ui.button(
                "Recargar",
                on_click=cargar_productos,
            )

        # ==========================================================
        # CARGA INICIAL
        # ==========================================================

        cargar_productos()