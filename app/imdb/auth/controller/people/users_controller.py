from imdb.auth.service import user_service
from imdb.auth.controller.general_controller import GeneralController


class UserController(GeneralController):
    """
    Realisation of Country controller.
    """

    _service = user_service
