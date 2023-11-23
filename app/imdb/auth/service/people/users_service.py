from imdb.auth.dao import user_dao
from imdb.auth.service.general_service import GeneralService


class UserService(GeneralService):
    """
    Realisation of users service.
    """

    _dao = user_dao
