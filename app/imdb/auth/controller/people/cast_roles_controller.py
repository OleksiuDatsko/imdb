from imdb.auth.service import cast_role_service
from imdb.auth.controller.general_controller import GeneralController


class CastRoleController(GeneralController):
    """
    Realisation of Country controller.
    """

    _service = cast_role_service
    
    def find_cast_role_film_crew_people(self, id):
        return [film.put_into_dto() for film in self._service.find_cast_role_film_crew_people(id)]
