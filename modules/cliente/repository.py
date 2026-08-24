from sqlalchemy import select

from core.database import SessionLocal
from models.cliente import Cliente

class ClienteRepository:
    def crear_cliente(self, cliente):
        with SessionLocal() as session:

            session.add(cliente)
            session.commit()
            session.refresh(cliente)
            
            return cliente

    def obtener_clientes():
        with SessionLocal() as session:
            stmt = (
                select(Cliente)
                .order_by(Cliente.id.desc())
                .limit(10)
            )

            return session.scalars(stmt).all()


    def obtener_recipientes():
        with SessionLocal() as db:
            recipientes = db.query(Cliente).all()
            return recipientes
