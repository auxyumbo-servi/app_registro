from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import ForeignKey

from models.base import BaseModel


class DetalleRegistro(BaseModel):

    __tablename__ = "detella_registro"
    #registro_id--> models/registro
    registro_id: Mapped[int] = mapped_column(
        ForeignKey(
            "registro.id"
        )
    )
    #recipiente --> models/recipiente
    recipiente: Mapped[int]

    cantidad: Mapped[float]#detalle

    observacion: Mapped[str]#detalle


    registros: Mapped["Registro"] = relationship(
        "Registro",
        back_populates="detalles"
    )




