from __future__ import annotations
from typing import Any

from imdb import db
from imdb.auth.domain.i_dto import IDto


from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship



class User(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    info = Column(String(255))

    country_id = Column(Integer, ForeignKey("country.id"))
    country = relationship("Country", back_populates="users")
    reviews = relationship("Review", back_populates="user")

    def __repr__(self) -> str:
        return f"User('{self.id}', '{self.first_name}', '{self.last_name}', '{self.info}', '{self.country_id}', '{self.country}')"

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
            "country_id": self.country_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> User:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = User(
            id=dto_dict.get("id"),
            first_name=dto_dict.get("first_name"),
            last_name=dto_dict.get("last_name"),
            info=dto_dict.get("info"),
            country_id=dto_dict.get("country_id"),
        )
        return obj
