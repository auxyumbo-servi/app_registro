from sqlalchemy import select

from core.database import SessionLocal
from models.recipiente import Recipiente


class RecipienteRepository:

    @staticmethod
    def crear_recipiente(recipiente: Recipiente):
        with SessionLocal() as session:
            session.add(recipiente)
            session.commit()
            session.refresh(recipiente)
            return recipiente

    @staticmethod
    def obtener_recipientes():
        with SessionLocal() as session:
            stmt = (
                select(Recipiente)
                .order_by(Recipiente.id.desc())
            )

            return session.scalars(stmt).all()

    @staticmethod
    def obtener_recipiente(recipiente_id: int):
        with SessionLocal() as session:
            stmt = select(Recipiente).where(
                Recipiente.id == recipiente_id
            )

            return session.scalars(stmt).first()