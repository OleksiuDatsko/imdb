import logging
from http import HTTPStatus

from flask import Blueprint, Response, jsonify, request, make_response
from imdb.auth.domain.films.genres import Genre

from imdb.auth.controller import genre_controller as controller

genre_bp = Blueprint("genres", __name__, url_prefix="/genres/")


@genre_bp.get("")
def get_all_genres() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(
        jsonify(controller.find_all(**request.args)),
        HTTPStatus.OK,
    )


@genre_bp.post("")
def create_coutry() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    genre = Genre.create_from_dto(content)
    controller.create(genre)
    return make_response(jsonify(genre.put_into_dto()), HTTPStatus.CREATED)


@genre_bp.get("/<int:id>")
def get_genre(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    genre = controller.find_by_id(id)
    return make_response(jsonify(genre), HTTPStatus.OK)


@genre_bp.get("/<int:id>/films")
def get_genre_films(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    films = controller.find_genre_films(id)
    print(films, flush=True)
    return make_response(jsonify(films), HTTPStatus.OK)


@genre_bp.put("/<int:genre_id>/films/<int:film_id>/")
def add_genre_to_film(genre_id: int, film_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    films = controller.put_genre_to_film(genre_id, film_id)
    print(films, flush=True)
    return make_response("Film genres updated", HTTPStatus.OK)


@genre_bp.put("/<int:id>")
def put_coutry(id: int) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    genre = Genre.create_from_dto(content)
    controller.update(id, genre)
    return make_response("Genre updated", HTTPStatus.OK)


@genre_bp.delete("/<int:id>")
def delete_client(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    controller.delete(id)
    return make_response("Genre deleted", HTTPStatus.OK)
