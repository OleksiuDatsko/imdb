from imdb.auth.dao import country_dao
from imdb.auth.service.general_service import GeneralService


class CountryService(GeneralService):
    """
    Realisation of Country service.
    """

    _dao = country_dao
