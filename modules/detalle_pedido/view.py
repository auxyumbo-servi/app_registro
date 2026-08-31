from nicegui import ui

from modules.usuario.usuario_controller import (
    UsuarioController,
)

from modules.producto.producto_controller import (
    ProductoController,
)

from modules.detalle_pedido.controller import (
    PedidoController,
)

class Pedidoview:
    @ui.page("/pedidos")
    def pedido_view():

        detalles = []

        # ==========================================================
        # USUARIOS
        # ==========================================================

        usuarios = UsuarioController.listar()

        usuarios_options = {
            usuario.id: usuario.nombre
            for usuario in usuarios
        }

        usuario_select = ui.select(
            options=usuarios_options,
            label="Usuario",
        ).classes("w-80")

        # ==========================================================
        # PRODUCTOS
        # ==========================================================

        productos = ProductoController.listar()

        productos_options = {
            producto.id: (
                f"{producto.nombre} - "
                f"${producto.precio:.2f}"
            )
            for producto in productos
        }

        producto_select = ui.select(
            options=productos_options,
            label="Producto",
        ).classes("w-80")

        cantidad_input = ui.number(
            label="Cantidad",
            value=1,
            min=1,
            precision=0,
        )

        # ==========================================================
        # AGREGAR PRODUCTO
        # ==========================================================
        def agregar_recipientes():

            recipiente_id = recipiente_input.value
            cantidad = cantidad_input.value

            if recipiente_id is None:
                ui.notify(
                    "Seleccione un producto",
                    type="warning",
                )
                return
            recipiente = ProductoController.obtener(
                            int(recipiente_id)
                        )
            if recipiente is None:
                            ui.notify(
                                "Producto no encontrado",
                                type="negative",
                            )
                            return
            pass

        def agregar_producto():

            producto_id = producto_select.value
            cantidad = cantidad_input.value

            if producto_id is None:
                ui.notify(
                    "Seleccione un producto",
                    type="warning",
                )
                return

            producto = ProductoController.obtener(
                int(producto_id)
            )

            if producto is None:
                ui.notify(
                    "Producto no encontrado",
                    type="negative",
                )
                return

            detalles.append(
                {
                    "producto_id": producto.id,
                    "producto": producto.nombre,
                    "cantidad": int(cantidad),
                    "precio": float(producto.precio),
                    "subtotal": (
                        float(producto.precio)
                        * int(cantidad)
                    ),
                }
            )

            actualizar_tabla()

        # ==========================================================
        # TABLA
        # ==========================================================

        tabla = ui.table(
            columns=[
                {
                    "name": "producto",
                    "label": "Producto",
                    "field": "producto",
                },
                {
                    "name": "cantidad",
                    "label": "Cantidad",
                    "field": "cantidad",
                },
                {
                    "name": "precio",
                    "label": "Precio",
                    "field": "precio",
                },
                {
                    "name": "subtotal",
                    "label": "Subtotal",
                    "field": "subtotal",
                },
            ],
            rows=[],
        ).classes("w-full")

        # ==========================================================
        # ACTUALIZAR TABLA
        # ==========================================================

        def actualizar_tabla():

            tabla.rows = [
                {
                    "producto": detalle["producto"],
                    "cantidad": detalle["cantidad"],
                    "precio": detalle["precio"],
                    "subtotal": detalle["subtotal"],
                }
                for detalle in detalles
            ]

            tabla.update()

        # ==========================================================
        # GUARDAR PEDIDO
        # ==========================================================

        def guardar():

            if usuario_select.value is None:

                ui.notify(
                    "Seleccione un usuario",
                    type="warning",
                )
                return

            if not detalles:

                ui.notify(
                    "Agregue al menos un producto",
                    type="warning",
                )
                return

            datos_detalles = [
                {
                    "producto_id": detalle["producto_id"],
                    "cantidad": detalle["cantidad"],
                    "precio": detalle["precio"],
                }
                for detalle in detalles
            ]

            pedido = PedidoController.crear_con_detalles(
                usuario_id=int(
                    usuario_select.value
                ),
                detalles=datos_detalles,
            )

            ui.notify(
                f"Pedido #{pedido.id} creado",
                type="positive",
            )

            detalles.clear()
            actualizar_tabla()

        # ==========================================================
        # BOTONES
        # ==========================================================

        ui.button(
            "Agregar producto",
            on_click=agregar_producto,
        )

        ui.button(
            "Guardar pedido",
            on_click=guardar,
            color="positive",
        )