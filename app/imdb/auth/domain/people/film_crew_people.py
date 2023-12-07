from __future__ import annotations
from typing import Any

from imdb import db
from imdb.auth.domain.i_dto import IDto


from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

film_film_crew_person_association = Table(
    "film_top_cast",
    db.Model.metadata,
    Column("film_id", Integer, ForeignKey("film.id"), primary_key=True),
    Column("film_crew_person_id", Integer, ForeignKey("film_crew_person.id"), primary_key=True),
)


class FilmCrewPerson(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """

    __tablename__ = "film_crew_person"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    info = Column(String(255))

    country_id = Column(Integer, ForeignKey("country.id"), nullable=False)
    country = relationship("Country", back_populates="film_crew_people")

    cast_role_id = Column(Integer, ForeignKey("cast_role.id"), nullable=False)
    cast_role = relationship("CastRole", back_populates="film_crew_people")

    films = relationship(
        "Film",
        secondary=film_film_crew_person_association,
        back_populates="film_crew_people",
    )

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        return f"FilmCrewPerson('{self.id}', '{self.first_name}', '{self.last_name}', '{self.info}', '{self.country_id}', '{self.country}', '{self.cast_role_id}', '{self.cast_role}')"

    def put_into_dto(self) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "info": self.info,
            "country": self.country.name,
            "cast_role": self.cast_role.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> FilmCrewPerson:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = FilmCrewPerson(
            id=dto_dict.get("id"),
            first_name=dto_dict.get("first_name"),
            last_name=dto_dict.get("last_name"),
            info=dto_dict.get("info"),
            country_id=dto_dict.get("country_id"),
            cast_role_id=dto_dict.get("cast_role_id"),
        )
        return obj
