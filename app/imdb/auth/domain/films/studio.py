from __future__ import annotations
from typing import Any

from imdb import db
from imdb.auth.domain.i_dto import IDto
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Table, ForeignKey


class Studio(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """

    __tablename__ = "studio"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45))


    def __repr__(self) -> str:
        return f"Studio('{self.id}', '{self.name}')"

    def put_into_dto(self) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "films": [film.name for film in self.films]
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Studio:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Studio(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
        )
        return obj
