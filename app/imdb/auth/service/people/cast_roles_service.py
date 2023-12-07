from http import HTTPStatus
from flask import abort
from imdb.auth.dao import cast_role_dao
from imdb.auth.service.general_service import GeneralService


class CastRoleService(GeneralService):
    """
    Realisation of CastRole service.
    """

    _dao = cast_role_dao

    def find_cast_role_film_crew_people(self, id):
        cast_role = self._dao.find_by_id(id)
        if cast_role is None:
            abort(HTTPStatus.NOT_FOUND)
        return cast_role.film_crew_people
