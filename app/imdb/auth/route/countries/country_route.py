import logging
from http import HTTPStatus

from flask import Blueprint, Response, jsonify, request, make_response
from imdb.auth.domain.countries.country import Country

from imdb.auth.controller import country_controller as controller

country_bp = Blueprint("countries", __name__, url_prefix="/countries/")


@country_bp.get("")
def get_all_coutries() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(
        jsonify(controller.find_all(**request.args)),
        HTTPStatus.OK,
    )


@country_bp.post("")
def create_coutry() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    country = Country.create_from_dto(content)
    controller.create(country)
    return make_response(jsonify(country.put_into_dto()), HTTPStatus.CREATED)


@country_bp.get("/<int:contry_id>")
def get_country(contry_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    country = controller.find_by_id(contry_id)
    return make_response(jsonify(country), HTTPStatus.OK)

@country_bp.get("/<int:contry_id>/films")
def get_country_films(contry_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    films = controller.find_country_films(contry_id)
    print(films, flush=True)
    return make_response(jsonify(films), HTTPStatus.OK)

@country_bp.get("/<int:contry_id>/film-crew-people")
def get_country_film_crew_people(contry_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    film_crew_people = controller.find_country_film_crew_people(contry_id)
    print(film_crew_people, flush=True)
    return make_response(jsonify(film_crew_people), HTTPStatus.OK)


@country_bp.put("/<int:contry_id>")
def put_coutry(contry_id: int) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    country = Country.create_from_dto(content)
    controller.update(contry_id, country)
    return make_response("Country updated", HTTPStatus.OK)


@country_bp.delete("/<int:contry_id>")
def delete_client(contry_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    controller.delete(contry_id)
    return make_response("Country deleted", HTTPStatus.OK)
