from .countries.country_service import CountryService
from .films.film_service import FilmService
from .films.interesting_facts_service import InterestingFactService
from .people.users_service import UserService
from .people.reviews_service import ReviewsService

country_service = CountryService()
film_service = FilmService()
interesting_facts_service = InterestingFactService()
user_service = UserService()
reviews_service = ReviewsService()