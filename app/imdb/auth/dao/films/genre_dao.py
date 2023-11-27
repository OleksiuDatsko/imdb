from typing import List

from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.films.genres import Genre


class GenreDAO(GeneralDAO):
    """
    Realisation of Genre data access layer.
    """

    _domain_type = Genre
