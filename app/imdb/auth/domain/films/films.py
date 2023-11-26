from __future__ import annotations
from tkinter.tix import Tree
from typing import Any
from xmlrpc.client import TRANSPORT_ERROR
from sqlalchemy import Column, Integer, String, Text, DECIMAL
from sqlalchemy.orm import relationship

from imdb import db
from imdb.auth.domain.i_dto import IDto

from .genres import Genre, film_genre_association
from ..countries.country import Country, film_country_association
from ..people.film_crew_people import FilmCrewPerson, film_film_crew_person_association


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
    film_crew_people = relationship(
        "FilmCrewPerson", secondary=film_film_crew_person_association, back_populates="films"
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
            "crew": [{"name": crew_person.name, "role": crew_person.cast_role.name} for crew_person in self.film_crew_people]
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Film:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        genres = db.session.query(Genre).filter(Genre.name.in_(dto_dict.get("genres_names"))).all()
        countries = db.session.query(Country).filter(Country.name.in_(dto_dict.get("countries_names"))).all()
        crew = db.session.query(FilmCrewPerson).filter(FilmCrewPerson.id.in_(dto_dict.get("crew_people_ids"))).all()
        
        print(dto_dict, flush=True)

        obj = Film(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            description=dto_dict.get("description"),
            point=dto_dict.get("point"),
            year=dto_dict.get("year"),
        )
        
        obj.countries = countries
        obj.genres=genres
        obj.film_crew_people = crew
        return obj
