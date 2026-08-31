from models.usuario import Usuario

from modules.base.repository_generic import (
    GenericRepository,
)


class UsuarioRepository(
    GenericRepository[Usuario]
):
    model = Usuario