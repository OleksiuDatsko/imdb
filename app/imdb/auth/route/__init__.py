from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .countries.country_route import country_bp
    from .films.film_route import film_bp
    from .films.interesting_facts_route import interesting_fact_bp
    from .films.genre_route import genre_bp
    from .people.user_route import user_bp
    from .people.reviews_route import review_bp
    from .people.cast_roles_route import cast_role_bp
    from .people.film_crew_people_route import film_crew_person_bp

    app.register_blueprint(country_bp)
    app.register_blueprint(film_bp)
    app.register_blueprint(interesting_fact_bp)
    app.register_blueprint(genre_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(film_crew_person_bp)
    app.register_blueprint(cast_role_bp)
