from __future__ import annotations
from typing import Any

from imdb import db
from imdb.auth.domain.i_dto import IDto


from sqlalchemy import Column, ForeignKey, Integer, String, Text, DECIMAL
from sqlalchemy.orm import relationship


class InterestingFact(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """

    __tablename__ = "interesting_fact"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45))
    more_info = Column(Text())

    film_id = Column(Integer, ForeignKey("film.id"))
    film = relationship(
        "Film", back_populates="interesting_facts"
    )  # only on the child class

    def __repr__(self) -> str:
        return f"InterestingFact('{self.id}', '{self.name}', '{self.more_info}', '{self.film_id}', '{self.film}')"

    def put_into_dto(self) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "more_info": self.more_info,
            "film_id": self.film_id,
            "film_name": self.film.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> InterestingFact:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = InterestingFact(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            more_info=dto_dict.get("more_info"),
            film_id=dto_dict.get("film_id"),
        )
        return obj
