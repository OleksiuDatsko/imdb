from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.people.reviews import Review


class ReviewDAO(GeneralDAO):
    """
    Realisation of Review data access layer.
    """

    _domain_type = Review

    def find_by_film(self, id) -> list:
        return (
            self._session.query(Review)
            .filter(Review.film_id == id)
            .order_by(Review.id)
            .all()
        )

    def find_by_user(self, user_id: int) -> object:
        return (
            self._session.query(Review)
            .filter(Review.user_id == user_id)
            .order_by(Review.id)
            .all()
        )
