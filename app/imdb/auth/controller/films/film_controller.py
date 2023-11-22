from imdb.auth.service import film_service
from imdb.auth.controller.general_controller import GeneralController


class FilmController(GeneralController):
    """
    Realisation of Country controller.
    """

    _service = film_service
