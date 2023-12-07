from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.people.users import User


class UserDAO(GeneralDAO):
    """
    Realisation of Country data access layer.
    """

    _domain_type = User
