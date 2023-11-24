from imdb.auth.service import genre_service
from imdb.auth.controller.general_controller import GeneralController


class GenreController(GeneralController):
    """
    Realisation of genre controller.
    """

    _service = genre_service
    
    def find_genre_films(self, id):
        return [film.put_into_dto() for film in self._service.find_genre_films(id)]
