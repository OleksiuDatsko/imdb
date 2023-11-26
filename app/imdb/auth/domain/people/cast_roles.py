from __future__ import annotations
from typing import Any

from imdb import db
from imdb.auth.domain.i_dto import IDto


from sqlalchemy import Column, ForeignKey, Integer, NotNullable, String
from sqlalchemy.orm import relationship

class CastRole(db.Model, IDto):
    __tablename__ = "cast_role"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45))

    film_crew_people = relationship("FilmCrewPerson", back_populates="cast_role")

    def __repr__(self) -> str:
        return f"CastRole('{self.id}', '{self.name}')"

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
    def create_from_dto(dto_dict: dict[str, Any]) -> CastRole:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = CastRole(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
        )
        return obj
