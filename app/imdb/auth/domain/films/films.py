from __future__ import annotations
import re
from typing import Any

from imdb import db
from imdb.auth.domain.i_dto import IDto


from sqlalchemy import Column, ForeignKey, Integer, String, Text, DECIMAL


class Film(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """

    __tablename__ = "film"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45))
    description = Column(Text())
    point = Column(DECIMAL(2, 1))
    year = Column(String(4))

    # country_id = Column(Integer, ForeignKey('country.id'))
    # country = db.relationship("Country", backref="country")  # only on the child class

    def __repr__(self) -> str:
        return f"Film('{self.id}', '{self.name}', '{self.description}', '{self.point}')"

    def put_into_dto(self, all=None) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "point": self.point,
            "year": self.year
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Film:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Film(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            description=dto_dict.get("description"),
            point=dto_dict.get("point"),
            year=dto_dict.get("year")
        )
        return obj
