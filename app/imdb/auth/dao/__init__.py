from .countries.country_dao import ContryDAO
from .films.film_dao import FilmDAO
from .films.interesting_facts_dao import InterestingFactDAO
from .people.users_dao import UserDAO
from .people.reviews_dao import ReviewDAO

country_dao = ContryDAO()
film_dao = FilmDAO()
interesting_fact_dao = InterestingFactDAO()
user_dao = UserDAO()
review_dao = ReviewDAO()