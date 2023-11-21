from typing import List

from imdb.auth.dao.general_dao import GeneralDAO
from imdb.auth.domain.countries.country import Country  

class ContryDAO(GeneralDAO):
    """
    Realisation of Country data access layer.
    """
    _domain_type = Country

    def find_by_name(self, name: str):
        """
        Gets Country objects from database table by name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Country).filter(Country.name == name).order_by(Country.name).all()
