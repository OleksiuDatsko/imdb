from .countries.country_controller import CountryController
from .films.film_controller import FilmController
from .films.interesting_facts_controller import InterestingFactController
from .people.users_controller import UserController

film_controller = FilmController()
interesting_facts_controler =  InterestingFactController()
country_controller = CountryController()
user_controller = UserController()
