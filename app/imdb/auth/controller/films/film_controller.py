from imdb.auth.service import film_service
from imdb.auth.controller.general_controller import GeneralController


class FilmController(GeneralController):
    """
    Realisation of Country controller.
    """

    _service = film_service

    def find_film_crew(self, id):
        return [person.put_into_dto() for person in self._service.find_film_crew(id)]
    
    def get_point_statistics(self, aggregate_type: str):
        print(self._service.get_point_statistics(aggregate_type)[0][0], flush=True)
        return self._service.get_point_statistics(aggregate_type)[0][0]
