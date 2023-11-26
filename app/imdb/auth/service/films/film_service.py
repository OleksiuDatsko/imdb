from http import HTTPStatus
from flask import abort
from imdb.auth.dao import film_dao
from imdb.auth.service.general_service import GeneralService


class FilmService(GeneralService):
    """
    Realisation of film service.
    """

    _dao = film_dao
    
    def find_film_crew(self, id):
        film = self._dao.find_by_id(id)
        if film is None:
            abort(HTTPStatus.NOT_FOUND)
        return film.film_crew_people

