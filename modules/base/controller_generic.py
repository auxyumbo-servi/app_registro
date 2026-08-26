from typing import Generic, TypeVar

from .service_generic import (
    GenericService,
)


T = TypeVar("T")


class GenericController(Generic[T]):
    service: type[GenericService[T]]

    @classmethod
    def listar(cls) -> list[T]:
        return cls.service.obtener_todos()

    @classmethod
    def obtener(
        cls,
        entity_id: int,
    ) -> T | None:

        return cls.service.obtener_por_id(
            entity_id
        )

    @classmethod
    def crear(cls, entity: T) -> T:
        return cls.service.crear(entity)

    @classmethod
    def actualizar(
        cls,
        entity_id: int,
        datos: dict,
    ) -> T | None:

        return cls.service.actualizar(
            entity_id,
            datos,
        )

    @classmethod
    def eliminar(
        cls,
        entity_id: int,
    ) -> bool:

        return cls.service.eliminar(
            entity_id
        )

    @classmethod
    def existe(
        cls,
        entity_id: int,
    ) -> bool:

        return cls.service.existe(
            entity_id
        )