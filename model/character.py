from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from model.base import Base


class Character(Base):
    __tablename__ = "Character"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    height: Mapped[int]
    mass: Mapped[int]
    hair_color: Mapped[str] = mapped_column(String(30))
    skin_color: Mapped[str] = mapped_column(String(30))
    eye_color: Mapped[str] = mapped_column(String(30))
    birth_year: Mapped[int]
