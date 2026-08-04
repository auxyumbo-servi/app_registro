from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from core.database import Base


class BaseModel(Base):

    __abstract__ = True


    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )