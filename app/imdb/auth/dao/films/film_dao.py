from sqlalchemy import text
from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.films.films import Film


class FilmDAO(GeneralDAO):
    """
    Realisation of Country data access layer.
    """

    _domain_type = Film
        
    def get_point_statistics(self, aggregate_type: str):
        return self._session.execute(text(f"CALL get_films_point_statistics('{aggregate_type}')")).all()
