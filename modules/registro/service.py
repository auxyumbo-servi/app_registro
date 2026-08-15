from sqlalchemy.orm import Session

from models.registro import Registro
from schemas.registro import RegistroCreate


def crear_registro(
    session: Session,
    data: RegistroCreate,
) -> Registro:

    registro = Registro(
        cliente_id=data.cliente_id,
    )

    session.add(registro)
    session.commit()
    session.refresh(registro)

    return registro
