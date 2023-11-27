from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.people.film_crew_people import FilmCrewPerson


class FilmCrewPersonDAO(GeneralDAO):
    """
    Realisation of Country data access layer.
    """

    _domain_type = FilmCrewPerson
