from http import HTTPStatus

from flask import Blueprint, Response, jsonify, request, make_response
from imdb.auth.domain.people.reviews import Review

from imdb.auth.controller import review_controller as controller


review_bp = Blueprint("reviews", __name__, url_prefix="/reviews/")


@review_bp.get("")
def get_all_reviews() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """

    return make_response(
        jsonify(controller.find_all()),
        HTTPStatus.OK,
    )


@review_bp.post("")
def create_review() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    review = Review.create_from_dto(content)
    controller.create(review)
    return make_response(jsonify(review.put_into_dto()), HTTPStatus.CREATED)


@review_bp.get("/<int:id>")
def get_review(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    review = controller.find_by_id(id)
    return make_response(jsonify(review), HTTPStatus.CREATED)


@review_bp.put("/<int:id>")
def put_review(id: int) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    review = Review.create_from_dto(content)
    controller.update(id, review)
    return make_response("Country updated", HTTPStatus.OK)


@review_bp.delete("/<int:id>")
def delete_client(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    controller.delete(id)
    return make_response("Country deleted", HTTPStatus.OK)
