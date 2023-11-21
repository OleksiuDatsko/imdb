from __future__ import annotations
from typing import Any

from imdb import db
from imdb.auth.domain.i_dto import IDto


class Country(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """

    __tablename__ = "country"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))

    def __repr__(self) -> str:
        return f"Country('{self.id}', '{self.name}')"

    def put_into_dto(self) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            # "id": self.id,
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
        )  # type: ignore
        return obj
