from __future__ import annotations
from typing import Any

from imdb import db
from imdb.auth.domain.i_dto import IDto
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Table, ForeignKey


film_country_association = Table(
    "film_country",
    db.Model.metadata,
    Column("film_id", Integer, ForeignKey("film.id")),
    Column("country_id", Integer, ForeignKey("country.id")),
)


class Country(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """

    __tablename__ = "country"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45))

    users = relationship("User", back_populates="country")
    film_crew_people = relationship("FilmCrewPerson", back_populates="country")

    films = relationship(
        "Film", secondary=film_country_association, back_populates="countries"
    )

    def __repr__(self) -> str:
        return f"Country('{self.id}', '{self.name}')"

    def put_into_dto(self, all: bool = None) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Country:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Country(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
        )
        return obj
