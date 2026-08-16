from sqlalchemy import select
from sqlalchemy.orm import Session

from models.recipiente import Recipiente
from schemas.recipiente import RecipienteCreate


def crear_recipiente(
    session: Session,
    data: RecipienteCreate,
) -> Recipiente:

    recipiente = Recipiente(
        nombre=data.nombre,
        equivalencia=data.equivalencia,
    )

    session.add(recipiente)
    session.commit()
    session.refresh(recipiente)

    return recipiente
