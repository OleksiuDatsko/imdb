from http import HTTPStatus
from flask import abort
from imdb.auth.dao import film_crew_person_dao
from imdb.auth.service.general_service import GeneralService


class FilmCrewPersonService(GeneralService):
    """
    Realisation of film crew people service.
    """

    _dao = film_crew_person_dao
    
    def find_crew_person_films(self, id):
        crew_person = self._dao.find_by_id(id)
        if crew_person is None:
            abort(HTTPStatus.NOT_FOUND)
        return crew_person.films
