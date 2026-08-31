from typing import Generic, TypeVar

from .repository_generic import (
    GenericRepository,
)


T = TypeVar("T")


class GenericService(Generic[T]):
    repository: type[GenericRepository[T]]

    @classmethod
    def crear(cls, entity: T) -> T:
        return cls.repository.crear(entity)

    @classmethod
    def obtener_todos(cls) -> list[T]:
        return cls.repository.obtener_todos()

    @classmethod
    def obtener_por_id(
        cls,
        entity_id: int,
    ) -> T | None:

        return cls.repository.obtener_por_id(
            entity_id
        )

    @classmethod
    def actualizar(
        cls,
        entity_id: int,
        datos: dict,
    ) -> T | None:

        return cls.repository.actualizar(
            entity_id,
            datos,
        )

    @classmethod
    def eliminar(
        cls,
        entity_id: int,
    ) -> bool:

        return cls.repository.eliminar(
            entity_id
        )

    @classmethod
    def existe(
        cls,
        entity_id: int,
    ) -> bool:

        return cls.repository.existe(
            entity_id
        )