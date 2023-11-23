from http import HTTPStatus

from flask import Blueprint, Response, jsonify, request, make_response
from imdb.auth.domain.people.users import User

from imdb.auth.controller import user_controller as controller

# from imdb.auth.controller import interesting_facts_controler as additional_controller


user_bp = Blueprint("users", __name__, url_prefix="/users/")


@user_bp.get("")
def get_all_users() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """

    return make_response(
        jsonify(controller.find_all()),
        HTTPStatus.OK,
    )


@user_bp.post("")
def create_user() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    user = User.create_from_dto(content)
    controller.create(user)
    return make_response(jsonify(user.put_into_dto()), HTTPStatus.CREATED)


@user_bp.get("/<int:id>")
def get_user(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    user = controller.find_by_id(id)
    return make_response(jsonify(user), HTTPStatus.CREATED)


@user_bp.put("/<int:id>")
def put_user(id: int) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    user = User.create_from_dto(content)
    controller.update(id, user)
    return make_response("Country updated", HTTPStatus.OK)


@user_bp.delete("/<int:id>")
def delete_client(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    controller.delete(id)
    return make_response("Country deleted", HTTPStatus.OK)
