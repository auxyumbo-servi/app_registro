from models.usuario import Usuario

from modules.base.controller_generic import (
    GenericController,
)

from .usuario_service import (
    UsuarioService,
)


class UsuarioController(
    GenericController[Usuario]
):
    service = UsuarioService