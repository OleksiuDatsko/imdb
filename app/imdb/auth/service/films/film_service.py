from imdb.auth.dao import film_dao
from imdb.auth.service.general_service import GeneralService


class FilmService(GeneralService):
    """
    Realisation of film service.
    """

    _dao = film_dao
