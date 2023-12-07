from .countries.country_service import CountryService
from .films.film_service import FilmService
from .films.interesting_facts_service import InterestingFactService
from .films.genre_service import GenreService
from .people.users_service import UserService
from .people.reviews_service import ReviewsService
from .people.cast_roles_service import CastRoleService
from .people.film_crew_people_service import FilmCrewPersonService

country_service = CountryService()
film_service = FilmService()
interesting_facts_service = InterestingFactService()
user_service = UserService()
reviews_service = ReviewsService()
genre_service = GenreService()
cast_role_service = CastRoleService()
film_crew_person_service = FilmCrewPersonService()
