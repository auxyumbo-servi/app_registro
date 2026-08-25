from sqlalchemy import select

from core.database import SessionLocal
from models.cliente import Cliente


class ClienteRepository:

    @staticmethod
    def crear_cliente(cliente: Cliente):
        with SessionLocal() as session:
            session.add(cliente)
            session.commit()
            session.refresh(cliente)
            return cliente

    @staticmethod
    def obtener_clientes():
        with SessionLocal() as session:
            stmt = (
                select(Cliente)
                .order_by(Cliente.id.desc())
            )

            return session.scalars(stmt).all()

    @staticmethod
    def obtener_cliente(cliente_id: int):
        with SessionLocal() as session:
            stmt = select(Cliente).where(
                Cliente.id == cliente_id
            )

            return session.scalars(stmt).first()