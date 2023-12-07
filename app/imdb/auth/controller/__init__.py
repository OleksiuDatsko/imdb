from .countries.country_controller import CountryController
from .films.film_controller import FilmController
from .films.interesting_facts_controller import InterestingFactController
from .films.genre_controller import GenreController
from .people.users_controller import UserController
from .people.reviews_controller import ReviewsController
from .people.cast_roles_controller import CastRoleController
from .people.film_crew_people_controller import FilmCrewPersonController

film_controller = FilmController()
interesting_facts_controler = InterestingFactController()
country_controller = CountryController()
user_controller = UserController()
review_controller = ReviewsController()
genre_controller = GenreController()
cast_role_controller = CastRoleController()
film_crew_person_controller = FilmCrewPersonController()
