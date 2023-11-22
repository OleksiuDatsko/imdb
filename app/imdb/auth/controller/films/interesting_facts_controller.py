from http import HTTPStatus
from flask import abort
from imdb.auth.service import interesting_facts_service
from imdb.auth.controller.general_controller import GeneralController


class InterestingFactController(GeneralController):
    """
    Realisation of interesting fact controller.
    """

    _service = interesting_facts_service
    
    def find_by_film(self, id: int) -> object:
        """
        Gets object from database table by integer key using from Service layer.
        :param key: integer key (surrogate primary key)
        :return: DTO for search object
        """
        return list(map(lambda x: x.put_into_dto(), self._service.find_by_film(id)))