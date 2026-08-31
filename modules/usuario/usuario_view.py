from nicegui import ui

import time

from .usuario_controller import UsuarioController
from models.usuario import Usuario
from schemas.helper import focus

contador_tab = 0
ultimo_tab = 0


class UsuarioView:
    @ui.page("/usuarios")
    def usuario_view():

        ui.label("Gestión de Usuarios").classes(
            "text-2xl font-bold mb-4"
        )

        # ==========================================================
        # CAMPOS DEL FORMULARIO
        # ==========================================================

        with ui.row().classes("items-end"):

            nombre_input = ui.input(
                label="Nombre"
            )

            email_input = ui.input(
                label="email",
                
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
                    "name": "email",
                    "label": "email",
                    "field": "email",
                },
            ],
            rows=[],
            row_key="id",
        ).classes("w-full")

        # ==========================================================
        # CARGAR usuarios
        # ==========================================================

        def cargar_usuarios():

            usuarios = UsuarioController.listar()

            tabla.rows = [
                {
                    "id": usuario.id,
                    "nombre": usuario.nombre,
                    "email": usuario.email,
                }
                for usuario in usuarios
            ]

            tabla.update()

        # ==========================================================
        # CREAR
        # ==========================================================

        def crear():

            nombre = nombre_input.value
            email = email_input.value

            if not nombre:
                ui.notify(
                    "El nombre es obligatorio",
                    type="warning",
                )
                return

            if email is None:
                ui.notify(
                    "El email es obligatorio",
                    type="warning",
                )
                return

            try:

                usuario = Usuario(
                    nombre=nombre,
                    email=email,
                )

                UsuarioController.crear(usuario)

                ui.notify(
                    "Usuario creado correctamente",
                    type="positive",
                )

                nombre_input.value = ""
                email_input.value = None

                cargar_usuarios()

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

                usuario_id = int(id_input.value)

                usuario = UsuarioController.obtener(
                    usuario_id
                )

                if usuario is None:

                    ui.notify(
                        "Usuario no encontrado",
                        type="warning",
                    )

                    return

                nombre_input.value = usuario.nombre
                email_input.value = usuario.email

                ui.notify(
                    f"Usuario encontrado: {usuario.nombre}",
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

                usuario_id = int(id_input.value)

                datos = {
                    "nombre": nombre_input.value,
                    "email": email_input.value,
                }

                usuario = UsuarioController.actualizar(
                    usuario_id,
                    datos,
                )

                if usuario is None:

                    ui.notify(
                        "Usuario no encontrado",
                        type="warning",
                    )

                    return

                ui.notify(
                    "Usuario actualizado correctamente",
                    type="positive",
                )

                cargar_usuarios()

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

                usuario_id = int(id_input.value)

                eliminado = UsuarioController.eliminar(
                    usuario_id
                )

                if not eliminado:

                    ui.notify(
                        "Usuario no encontrado",
                        type="warning",
                    )

                    return

                ui.notify(
                    "Usuario eliminado correctamente",
                    type="positive",
                )

                nombre_input.value = ""
                email_input.value = None

                cargar_usuarios()

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
                label="ID del usuario",
                min=1,
                precision=0,
            )

            campo = ui.input("Campo")

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
                "Crear usuario",
                on_click=crear,
                color="primary",
            )

            ui.button(
                "Recargar",
                on_click=cargar_usuarios,
            )

        # ==========================================================
        # CARGA INICIAL
        # =========================================================

        
        def procesar_tab(e):
            global contador_tab, ultimo_tab

            ahora = time.monotonic()

            # Si pasó más de 500 ms, empezamos nuevamente
            if ahora - ultimo_tab > 2:
                contador_tab = 0

            contador_tab += 1
            ultimo_tab = ahora

            if contador_tab == 1:
                obtener_por_id()
                

            elif contador_tab == 2:
                crear()
                contador_tab = 0        
                focus('id_input')

        campo.on(
            'keydown',
            lambda e: procesar_tab(e)
            if e.args.get('key') == 'Tab'
            else None
        )  
        
        cargar_usuarios()