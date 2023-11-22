from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.films.films import Film


class FilmDAO(GeneralDAO):
    """
    Realisation of Country data access layer.
    """

    _domain_type = Film

    def find_by_name(self, name: str) -> list:
        """
        Gets Country objects from database table by name.
        :param name: name value
        :return: search objects
        """
        return (
            self._session.query(Film)
            .filter(Film.name == name)
            .order_by(Film.name)
            .all()
        )
