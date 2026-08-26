from models.usuario import Usuario

from .usuario_repository import (
    UsuarioRepository,
)

from modules.base.service_generic import (
    GenericService,
)


class UsuarioService(
    GenericService[Usuario]
):
    repository = UsuarioRepository