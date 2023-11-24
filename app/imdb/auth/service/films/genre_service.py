from http import HTTPStatus
from flask import abort
from imdb.auth.dao import genre_dao
from imdb.auth.service.general_service import GeneralService


class GenreService(GeneralService):
    """
    Realisation of genre service.
    """

    _dao = genre_dao

    def find_genre_films(self, id):
        genre = self._dao.find_by_id(id)
        if genre is None:
            abort(HTTPStatus.NOT_FOUND)
        return genre.films
