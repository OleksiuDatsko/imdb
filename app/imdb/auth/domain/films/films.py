from __future__ import annotations
from typing import Any
from sqlalchemy import Column, Integer, String, Text, DECIMAL
from sqlalchemy.orm import relationship

from imdb import db
from imdb.auth.domain.i_dto import IDto

from .genres import film_genre_association
from ..countries.country import film_country_association


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

    # 1:M
    interesting_facts = relationship(
        "InterestingFact", back_populates="film", cascade="all, delete-orphan"
    )
    reviews = relationship(
        "Review", back_populates="film", cascade="all, delete-orphan"
    )

    # M:M
    countries = relationship(
        "Country", secondary=film_country_association, back_populates="films"
    )
    genres = relationship(
        "Genre", secondary=film_genre_association, back_populates="films"
    )

    def __repr__(self) -> str:
        return f"Film('{self.id}', '{self.name}', '{self.description}', '{self.point}')"

    def put_into_dto(self) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "point": self.point,
            "year": self.year,
            "genres": [genre.name for genre in self.genres],
            "countries": [country.name for country in self.countries],
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
            year=dto_dict.get("year"),
        )
        return obj
