from http import HTTPStatus

from flask import Blueprint, Response, jsonify, request, make_response
from imdb.auth.domain.people.cast_roles import CastRole

from imdb.auth.controller import cast_role_controller as controller

cast_role_bp = Blueprint("cast_roles", __name__, url_prefix="/cast-roles/")


@cast_role_bp.get("")
def get_all_coutries() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(
        jsonify(controller.find_all(**request.args)),
        HTTPStatus.OK,
    )


@cast_role_bp.post("")
def create_coutry() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    cast_role = CastRole.create_from_dto(content)
    controller.create(cast_role)
    return make_response(jsonify(cast_role.put_into_dto()), HTTPStatus.CREATED)


@cast_role_bp.get("/<int:id>")
def get_cast_role(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    cast_role = controller.find_by_id(id)
    return make_response(jsonify(cast_role), HTTPStatus.OK)


@cast_role_bp.get("/<int:id>/film-crew-people")
def get_cast_role_film_crew_people(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    film_crew_people = controller.find_cast_role_film_crew_people(id)
    print(film_crew_people, flush=True)
    return make_response(jsonify(film_crew_people), HTTPStatus.OK)


@cast_role_bp.put("/<int:id>")
def put_coutry(id: int) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    cast_role = CastRole.create_from_dto(content)
    controller.update(id, cast_role)
    return make_response("Country updated", HTTPStatus.OK)


@cast_role_bp.delete("/<int:id>")
def delete_client(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    controller.delete(id)
    return make_response("Country deleted", HTTPStatus.OK)
