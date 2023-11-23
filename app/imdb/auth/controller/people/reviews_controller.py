from imdb.auth.service import reviews_service
from imdb.auth.controller.general_controller import GeneralController


class ReviewsController(GeneralController):
    """
    Realisation of Country controller.
    """

    _service = reviews_service

    def find_by_user(self, id: int) -> object:
        """
        Gets object from database table by integer key using from Service layer.
        :param key: integer key (surrogate primary key)
        :return: DTO for search object
        """
        return list(map(lambda x: x.put_into_dto(), self._service.find_by_user(id)))
    
    def find_by_film(self, id: int) -> object:
        """
        Gets object from database table by integer key using from Service layer.
        :param key: integer key (surrogate primary key)
        :return: DTO for search object
        """
        return list(map(lambda x: x.put_into_dto(), self._service.find_by_film(id)))