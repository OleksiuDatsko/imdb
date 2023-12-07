from typing import List

from sqlalchemy import text

from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.films.genres import Genre

from imdb import db


class GenreDAO(GeneralDAO):
    """
    Realisation of Genre data access layer.
    """

    _domain_type = Genre
    _session = db.session
    
    def create(self, obj: object) -> object:
        """
        Creates object in database table.
        :param obj: object to create in Database
        :return: created object
        """
        self._session.execute(text(f"CALL insert_genre('{obj.name}')"))
        self._session.commit()
        return obj
    
    def update_films_genres(self, genre_id, film_id):
        self._session.execute(text(f"CALL insert_film_genre({film_id}, {genre_id})"))
        self._session.commit()

