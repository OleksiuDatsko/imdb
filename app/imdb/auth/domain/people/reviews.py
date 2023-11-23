from __future__ import annotations
from datetime import datetime
import time
from typing import Any

from imdb import db
from imdb.auth.domain.i_dto import IDto


from sqlalchemy import Column, Date, ForeignKey, Integer, String


class Review(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """

    __tablename__ = "review"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    comment = Column(String(255))
    mark = Column(Integer)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = db.relationship("User", backref="review_user")
    
    film_id = Column(Integer, ForeignKey("film.id"))
    film = db.relationship("Film", backref="review_film")
    

    def __repr__(self) -> str:
        return f"Review('{self.id}', '{self.date}', '{self.comment}', '{self.mark}', '{self.user_id}', '{self.film_id}', '{self.user}', '{self.film}')"

    def put_into_dto(self) -> dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "date": self.date,
            "comment": self.comment,
            "mark": self.mark,
            "user_id": self.user_id,
            "film_id": self.film_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Review:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Review(
            date=dto_dict.get("date") or datetime.now(),
            comment=dto_dict.get("comment"),
            mark=dto_dict.get("mark"),
            user_id=dto_dict.get("user_id"),
            film_id=dto_dict.get("film_id"),
        )
        return obj
