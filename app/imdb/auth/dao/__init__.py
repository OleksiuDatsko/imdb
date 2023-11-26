from .countries.country_dao import ContryDAO
from .films.film_dao import FilmDAO
from .films.interesting_facts_dao import InterestingFactDAO
from .films.genre_dao import GenreDAO
from .people.users_dao import UserDAO
from .people.reviews_dao import ReviewDAO
from .people.cast_roles_dao import CastRoleDAO
from .people.film_crew_people_dao import FilmCrewPersonDAO

country_dao = ContryDAO()
film_dao = FilmDAO()
interesting_fact_dao = InterestingFactDAO()
user_dao = UserDAO()
review_dao = ReviewDAO()
genre_dao = GenreDAO()
cast_role_dao = CastRoleDAO()
film_crew_person_dao = FilmCrewPersonDAO()
