from imdb.auth.service import film_service
from imdb.auth.controller.general_controller import GeneralController


class FilmController(GeneralController):
    """
    Realisation of Country controller.
    """

    _service = film_service
    
    def find_film_crew(self, id):
        return [person.put_into_dto() for person in self._service.find_film_crew(id)]
