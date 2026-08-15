from sqlalchemy.orm import Session

from models.cliente import Cliente
from schemas.cliente import ClienteCreate


def crear_cliente(
    session: Session,
    data: ClienteCreate,
) -> Cliente:

    cliente = Cliente(
        nombre=data.nombre,
        contrato=data.contrato,
    )

    session.add(cliente)
    session.commit()
    session.refresh(cliente)

    return cliente
