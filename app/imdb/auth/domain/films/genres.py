from __future__ import annotations
from typing import Any

from imdb import db
from imdb.auth.domain.i_dto import IDto


from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship


film_genre_association = Table(
    'film_genre',
    db.Model.metadata,
    Column('film_id', Integer, ForeignKey('film.id')),
    Column('genre_id', Integer, ForeignKey('genre.id'))
)

class Genre(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """

    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45))
    
    films = relationship("Film", secondary=film_genre_association, back_populates="genres")

    def __repr__(self) -> str:
        return f"Genre('{self.id}', '{self.name}', '{self.films}')"

    def put_into_dto(self) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Genre:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Genre(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
        )
        return obj
