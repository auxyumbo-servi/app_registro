from decimal import Decimal

from sqlalchemy.orm import Session

from models.detalle_registro import DetalleRegistro
from models.recipiente import Recipiente
from models.registro import Registro
from schemas.detalle_registro import DetalleRegistroCreate


def crear_detalle(
    session: Session,
    data: DetalleRegistroCreate,
) -> DetalleRegistro:

    registro = session.get(
        Registro,
        data.registro_id,
    )

    if registro is None:
        raise ValueError(
            "El registro no existe"
        )

    recipiente = session.get(
        Recipiente,
        data.recipiente_id,
    )

    if recipiente is None:
        raise ValueError(
            "El recipiente no existe"
        )

    subtotal = (
        data.cantidad
        * data.precio_unitario
    )

    detalle = DetalleRegistro(
        registro_id=data.registro_id,
        recipiente_id=data.recipiente_id,
        cantidad=data.cantidad,
        precio_unitario=data.precio_unitario,
        subtotal=subtotal,
    )

    session.add(detalle)
    session.commit()
    session.refresh(detalle)

    return detalle
