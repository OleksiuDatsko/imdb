from imdb.auth.service import film_crew_person_service
from imdb.auth.controller.general_controller import GeneralController


class FilmCrewPersonController(GeneralController):
    """
    Realisation of film crew people controller.
    """

    _service = film_crew_person_service

    def find_crew_person_films(self, id):
        return [
            film.put_into_dto() for film in self._service.find_crew_person_films(id)
        ]
