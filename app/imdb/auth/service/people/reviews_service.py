from imdb.auth.dao import review_dao
from imdb.auth.service.general_service import GeneralService


class ReviewsService(GeneralService):
    """
    Realisation of reviewss service.
    """

    _dao = review_dao

    def find_by_film(self, id) -> object:
        return self._dao.find_by_film(id)

    def find_by_user(self, id) -> object:
        return self._dao.find_by_user(id)
