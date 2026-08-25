from typing import Generic, Type, TypeVar

from sqlalchemy import select

from core.database import SessionLocal


T = TypeVar("T")


class GenericRepository(Generic[T]):

    model: Type[T]

    @classmethod
    def crear(cls, entity: T) -> T:
        with SessionLocal() as session:
            session.add(entity)
            session.commit()
            session.refresh(entity)

            return entity

    @classmethod
    def obtener_todos(cls) -> list[T]:
        with SessionLocal() as session:
            stmt = (
                select(cls.model)
                .order_by(cls.model.id.desc())
            )

            return session.scalars(stmt).all()

    @classmethod
    def obtener_por_id(
        cls,
        entity_id: int
    ) -> T | None:

        with SessionLocal() as session:
            stmt = select(cls.model).where(
                cls.model.id == entity_id
            )

            return session.scalars(stmt).first()

    @classmethod
    def actualizar(
        cls,
        entity_id: int,
        datos: dict
    ) -> T | None:

        with SessionLocal() as session:

            stmt = select(cls.model).where(
                cls.model.id == entity_id
            )

            entity = session.scalars(stmt).first()

            if entity is None:
                return None

            for campo, valor in datos.items():
                setattr(entity, campo, valor)

            session.commit()
            session.refresh(entity)

            return entity

    @classmethod
    def eliminar(
        cls,
        entity_id: int
    ) -> bool:

        with SessionLocal() as session:

            stmt = select(cls.model).where(
                cls.model.id == entity_id
            )

            entity = session.scalars(stmt).first()

            if entity is None:
                return False

            session.delete(entity)
            session.commit()

            return True

    @classmethod
    def existe(
        cls,
        entity_id: int
    ) -> bool:

        with SessionLocal() as session:

            stmt = select(cls.model).where(
                cls.model.id == entity_id
            )

            return session.scalars(stmt).first() is not None