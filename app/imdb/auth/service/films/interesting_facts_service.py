from imdb.auth.dao import interesting_fact_dao
from imdb.auth.service.general_service import GeneralService


class InterestingFactService(GeneralService):
    """
    Realisation of interesting fact service.
    """

    _dao = interesting_fact_dao

    def find_by_film(self, id) -> object:
        return self._dao.find_by_film(id)