import time
import uuid

from nicegui import ui


# ==========================================================
# FOCUS GENÉRICO
# ==========================================================

def focus_input(campo):
    """
    Pone el foco en cualquier componente NiceGUI.

    Ejemplo:
        focus_input(nombre_input)
        focus_input(id_input)
    """

    identificador = f"focus-{uuid.uuid4().hex}"

    campo.classes(identificador)

    ui.run_javascript(f"""
        const componente = document.querySelector('.{identificador}');

        if (componente) {{
            const input = componente.querySelector('input');

            if (input) {{
                input.focus();
            }}
        }}
    """)


# ==========================================================
# TAB GENÉRICO
# ==========================================================

def procesar_tab(
    e,
    campo_origen,
    campo_destino,
    funcion_1=None,
    funcion_2=None,
    tiempo=2,
):
    """
    Control genérico de TAB.

    Primer TAB:
        ejecuta funcion_1
        y mantiene el foco en campo_origen

    Segundo TAB:
        ejecuta funcion_2
        y mueve el foco a campo_destino

    tiempo:
        segundos máximos entre TAB y TAB.
    """

    # Solo nos interesa TAB
    if e.args.get("key") != "Tab":
        return

    # Guardamos el estado directamente en el componente origen
    if not hasattr(campo_origen, "_tab_contador"):
        campo_origen._tab_contador = 0
        campo_origen._ultimo_tab = 0

    ahora = time.monotonic()

    # Si pasó demasiado tiempo,
    # comenzamos nuevamente
    if ahora - campo_origen._ultimo_tab > tiempo:
        campo_origen._tab_contador = 0

    campo_origen._tab_contador += 1
    campo_origen._ultimo_tab = ahora

    contador = campo_origen._tab_contador

    print(f"TAB detectado: {contador}")

    # ======================================================
    # PRIMER TAB
    # ======================================================

    if contador == 1:

        if funcion_1:
            funcion_1()

        # Mantener el foco en el campo origen
        focus_input(campo_origen)

    # ======================================================
    # SEGUNDO TAB
    # ======================================================

    elif contador == 2:

        if funcion_2:
            funcion_2()

        # Reiniciar contador
        campo_origen._tab_contador = 0

        # Pasar al campo destino
        focus_input(campo_destino)

''' forma de llamar la funcion para procesar
        campo.on( #<------ campo hace referencia al nombre del campo donde nace todo (campo de origen)
                "keydown",
                lambda e: procesar_tab(
                    e,
                    campo_origen=date,
                    campo_destino=campo,
                    funcion_1=obtener_por_id,
                    funcion_2=crear,
                    tiempo=.5,
                )
            )'''