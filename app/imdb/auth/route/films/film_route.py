import logging
from http import HTTPStatus

from flask import Blueprint, Response, jsonify, request, make_response
from imdb.auth.domain.films.films import Film

from imdb.auth.controller import film_controller as controller
from imdb.auth.controller import interesting_facts_controler
from imdb.auth.controller import review_controller


film_bp = Blueprint("films", __name__, url_prefix="/films/")


@film_bp.get("")
def get_all_films() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """

    return make_response(
        jsonify(controller.find_all()),
        HTTPStatus.OK,
    )
    
@film_bp.get("<string:aggregate_type>/point")
def get_all_films_point_statistics(aggregate_type: str) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """

    return make_response(
        jsonify(controller.get_point_statistics(aggregate_type)),
        HTTPStatus.OK,
    )


@film_bp.post("")
def create_film() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    film = Film.create_from_dto(content)
    controller.create(film)
    return make_response(jsonify(film.put_into_dto()), HTTPStatus.CREATED)


@film_bp.get("/<int:id>")
def get_film(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    film = controller.find_by_id(id)
    return make_response(jsonify(film), HTTPStatus.OK)


@film_bp.get("/<int:id>/interesting-facts/")
def get_interesting_facts_of_film(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    interesting_facts = interesting_facts_controler.find_by_film(id)
    print(interesting_facts, flush=True)
    return make_response(jsonify(interesting_facts), HTTPStatus.CREATED)


@film_bp.get("/<int:id>/reviews/")
def get_reviews_of_film(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    reviews = review_controller.find_by_film(id)
    print(reviews, flush=True)
    return make_response(jsonify(reviews), HTTPStatus.CREATED)


@film_bp.get("/<int:id>/crew/")
def get_crew_of_film(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    crew = controller.find_film_crew(id)
    print(crew, flush=True)
    return make_response(jsonify(crew), HTTPStatus.CREATED)


@film_bp.put("/<int:id>")
def put_film(id: int) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    film = Film.create_from_dto(content)
    controller.update(id, film)
    return make_response("Country updated", HTTPStatus.OK)


@film_bp.delete("/<int:id>")
def delete_client(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    controller.delete(id)
    return make_response("Country deleted", HTTPStatus.OK)
