from http import HTTPStatus

from flask import Blueprint, Response, jsonify, request, make_response
from imdb.auth.domain.people.film_crew_people import FilmCrewPerson

from imdb.auth.controller import film_crew_person_controller as controller


film_crew_person_bp = Blueprint("film_crew_people", __name__, url_prefix="/crew/")


@film_crew_person_bp.get("")
def get_all_film_crew_people() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """

    return make_response(
        jsonify(controller.find_all()),
        HTTPStatus.OK,
    )


@film_crew_person_bp.post("")
def create_film_crew_person() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    film_crew_person = FilmCrewPerson.create_from_dto(content)
    controller.create(film_crew_person)
    return make_response(jsonify(film_crew_person.put_into_dto()), HTTPStatus.CREATED)


@film_crew_person_bp.get("/<int:id>")
def get_film_crew_person(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    film_crew_person = controller.find_by_id(id)
    return make_response(jsonify(film_crew_person), HTTPStatus.CREATED)

@film_crew_person_bp.get("/<int:id>/films")
def get_crew_person_films(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    films = controller.find_crew_person_films(id)
    return make_response(jsonify(films), HTTPStatus.CREATED)


@film_crew_person_bp.put("/<int:id>")
def put_film_crew_person(id: int) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    film_crew_person = FilmCrewPerson.create_from_dto(content)
    controller.update(id, film_crew_person)
    return make_response("Country updated", HTTPStatus.OK)


@film_crew_person_bp.delete("/<int:id>")
def delete_client(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    controller.delete(id)
    return make_response("Country deleted", HTTPStatus.OK)
