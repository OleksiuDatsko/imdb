from typing import List

from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.people.cast_roles import CastRole


class CastRoleDAO(GeneralDAO):
    """
    Realisation of CastRole data access layer.
    """

    _domain_type = CastRole

    def find_by_name(self, name: str) -> list:
        """
        Gets CastRole objects from database table by name.
        :param name: name value
        :return: search objects
        """
        return (
            self._session.query(CastRole)
            .filter(CastRole.name == name)
            .order_by(CastRole.name)
            .all()
        )
