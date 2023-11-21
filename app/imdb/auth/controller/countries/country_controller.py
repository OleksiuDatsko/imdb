"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from imdb.auth.service import country_service
from imdb.auth.controller.general_controller import GeneralController


class CountryController(GeneralController):
    """
    Realisation of Country controller.
    """

    _service = country_service
