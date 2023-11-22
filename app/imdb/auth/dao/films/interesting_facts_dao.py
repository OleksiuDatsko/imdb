from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.films.interesting_facts import InterestingFact


class InterestingFactDAO(GeneralDAO):
    """
    Realisation of Country data access layer.
    """

    _domain_type = InterestingFact

    def find_by_name(self, name: str) -> list:
        """
        Gets Country objects from database table by name.
        :param name: name value
        :return: search objects
        """
        return (
            self._session.query(InterestingFact)
            .filter(InterestingFact.name == name)
            .order_by(InterestingFact.name)
            .all()
        )
    
    def find_by_film(self, id) -> list:
        return (
            self._session.query(InterestingFact)
            .filter(InterestingFact.film_id == id)
            .order_by(InterestingFact.name)
            .all()
        )
