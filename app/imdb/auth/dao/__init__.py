from .countries.country_dao import ContryDAO
from .films.film_dao import FilmDAO
from .films.interesting_facts_dao import InterestingFactDAO

country_dao = ContryDAO()
film_dao = FilmDAO()
interesting_fact_dao = InterestingFactDAO()