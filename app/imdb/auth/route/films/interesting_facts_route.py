from http import HTTPStatus

from flask import Blueprint, Response, jsonify, request, make_response
from imdb.auth.domain.films.interesting_facts import InterestingFact

from imdb.auth.controller import interesting_facts_controler

interesting_fact_bp = Blueprint("interesting_facts", __name__, url_prefix="/interesting-facts/")


@interesting_fact_bp.get("")
def get_all_coutries() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    
    return make_response(
        jsonify(interesting_facts_controler.find_all(**request.args)),
        HTTPStatus.OK,
    )


@interesting_fact_bp.post("")
def create_coutry() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    country = InterestingFact.create_from_dto(content)
    interesting_facts_controler.create(country)
    return make_response(jsonify(country.put_into_dto()), HTTPStatus.CREATED)


@interesting_fact_bp.get("/<int:id>")
def get_country(id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    country = interesting_facts_controler.find_by_id(id)
    return make_response(jsonify(country), HTTPStatus.OK)


@interesting_fact_bp.put("/<int:id>")
def put_coutry(id: int) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    country = InterestingFact.create_from_dto(content)
    interesting_facts_controler.update(id, country)
    return make_response("Country updated", HTTPStatus.OK)


@interesting_fact_bp.delete("/<int:id>")
def delete_client(contry_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    interesting_facts_controler.delete(contry_id)
    return make_response("Country deleted", HTTPStatus.OK)
