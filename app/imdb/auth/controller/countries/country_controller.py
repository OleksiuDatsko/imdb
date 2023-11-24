from imdb.auth.service import country_service
from imdb.auth.controller.general_controller import GeneralController


class CountryController(GeneralController):
    """
    Realisation of Country controller.
    """

    _service = country_service
    
    def find_country_films(self, id):
        return [film.put_into_dto() for film in self._service.find_country_films(id)]
