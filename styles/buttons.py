from nicegui import ui


def primary(text, action=None):

    btn = ui.button(
        text,
        on_click=action
    )

    btn.props(
        """
        text-color=black
        color=yellow-400
        rounded
        """
        
    )

    return btn