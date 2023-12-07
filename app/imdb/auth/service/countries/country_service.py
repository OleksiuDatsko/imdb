from http import HTTPStatus
from flask import abort
from imdb.auth.dao import country_dao
from imdb.auth.service.general_service import GeneralService


class CountryService(GeneralService):
    """
    Realisation of Country service.
    """

    _dao = country_dao

    def find_country_films(self, id):
        country = self._dao.find_by_id(id)
        if country is None:
            abort(HTTPStatus.NOT_FOUND)
        return country.films

    def find_country_film_crew_people(self, id):
        country = self._dao.find_by_id(id)
        if country is None:
            abort(HTTPStatus.NOT_FOUND)
        return country.film_crew_people
